
title = ""
language_tabs = []
toc_footers = []
includes = []
search = False


settings = {}
finalContent = ""

with open("source/index.html.md") as file_in:
    fileContent = ""
    lines = []

    settingsStartFound = False
    settingsEndFound = False

    lineNo = 0
    currentListCategory = ""
    currentList = []
    for line in file_in:
        fileContent += line
        stripped = line.strip()


        if lineNo == 0 and stripped == "---":
            settingsStartFound = True
        elif settingsStartFound and not settingsEndFound and stripped == "---":
            settingsEndFound == True
            fileContent = ""
        elif settingsStartFound and not settingsEndFound:


            colonSplit = stripped.split(":")
            hyphenSplit = stripped.split("-", 1)
            if len(colonSplit) == 2 and len(hyphenSplit) == 1:
                if len(currentList) > 0:
                    settings[currentListCategory] = currentList
                    currentList = []

                colonSetting = colonSplit[0].strip()
                colonSettingValue = colonSplit[1].strip()
                if colonSettingValue != "":
                    if colonSetting == "search":
                        if colonSettingValue == "true":
                            settings["search"] = True
                        elif colonSettingValue == "false":
                            settings["search"] = False
                    else:
                        settings[colonSetting] = colonSettingValue
                else:
                    # New List
                    currentListCategory = colonSetting
            else:
                # Potential list item
                if len(hyphenSplit) == 2:
                    if currentListCategory == "includes":
                       currentList.append("_" + hyphenSplit[1].strip() + ".md")
                    else:
                        currentList.append(hyphenSplit[1].strip())

        lines.append(line)
        lineNo += 1
    content = [x.strip() for x in lines]
    finalContent = fileContent

# Adding includes content
if "includes" in settings:
    for includedFile in settings["includes"]:
       with open("source/includes/" + includedFile) as file_in:
           finalContent += file_in.read()

# print("---FILE CONTENT---")
# print(finalContent)

# print("---SETTINGS---")
# print(settings)




import mistletoe
from mistletoe.slate_html_renderer import SlateHTMLRenderer

SlateHTMLRenderer.settings = settings

rendered = mistletoe.markdown(finalContent, SlateHTMLRenderer)

# print(rendered)

# f = open("_action_type_product_type_linker.html", "r+")
f = open("build/index.html", "w+")
f.write(rendered)
f.close()

print("Finished!!")
