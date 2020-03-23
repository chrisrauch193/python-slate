from misaka import Markdown, HtmlRenderer, BaseRenderer

htmlrndr = HtmlRenderer()
rndr = BaseRenderer()
htmlmd = Markdown(htmlrndr)
md = Markdown(rndr)

htmlparsed = htmlmd('some html text')
parsed = md('some text')

print(htmlparsed)
print(parsed)

