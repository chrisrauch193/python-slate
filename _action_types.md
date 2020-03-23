## <u>Action Type</u>
Contains details of the types of Action that a technician can take during a repair


### <u>The action_type object</u>

Field | Description
------:|:------------
__action_type_id__ <br><font color="DarkGray">_int_</font> <font color="Crimson">__(primary key)__</font> | A unique integer identifier for each action_type.
__name__ <br><font color="DarkGray">_string_</font> <font color="Crimson">(not-null,unique)</font> | 
__description__ <br><font color="DarkGray">_string_</font> <font color="Crimson"></font> | 
__label__ <br><font color="DarkGray">_string_</font> <font color="Crimson">(not-null,unique)</font> | 
__created_at__  <br><font color="DarkGray">_datetime_</font> | timestamp that the record was created at
__created_by__  <br><font color="DarkGray">_text_</font>| username of the user who created the record
__modified_at__ <br><font color="DarkGray">_datetime_</font>| timestamp that the record was last modified
__modified_by__ <br><font color="DarkGray">_text_</font>| user that last modified the record

<br>

Relationship | Description
-------------:|:------------
__action_type_product_type_linker__ | The associated action_type_product_type_linker
__repair_action_type_linker__ | The associated repair_action_type_linker


<hr>
<br>

> An example POST request. Note that `action_type_id`, `created_at`, `modified_at` and `created_by` are all handled internally by the system and need not be explicitly specified. See Meta Data for more information.

```python
    url = "https://smartapi.bboxx.co.uk/v1/action_types"
    data = json.dumps({
		"name": "test",
		"description": "test",
		"label": "test",
		})
    headers = {'Content-Type': 'application/json', 'Authorization': 'Token token=A_VALID_TOKEN'}

    r = requests.post(url=url, data=data, headers=headers)

    r
    >>> <Response 201>

    r.json()

    >>> {
		"action_type_id": 1
		"name": "test",
		"description": "test",
		"label": "test",
		"created_at": "2000-01-01 00:00:00"
		"created_by": "test.user@bboxx.co.uk"
		"modified_at": None
	}
```

    > We can retrieve the `action_type` created by specifying its `action_type_id` in the request url:

```python
    url = 'https://smartapi.bboxx.co.uk/v1/action_types/1'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Token token=A_VALID_TOKEN'}

    r = requests.get(url=url, headers=headers)

    r
    >>> <Response 200>

    r.json()
    >>> {
		"action_type_id": 1
		"name": "test",
		"description": "test",
		"label": "test",
		"created_at": "2000-01-01 00:00:00"
		"created_by": "test.user@bboxx.co.uk"
		"modified_at": None
	}
```

> We can retrieve all `action_types` by omitting the `action_type_id`:

```python
    url = 'https://smartapi.bboxx.co.uk/v1/action_types'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Token token=A_VALID_TOKEN'}

    r = requests.get(url=url, headers=headers)

    r
    >>> <Response 200>

    r.json()
    >>> {
        u'total_pages': 1,
        u'objects': [
            {<record>},
            {<record>},
            {<record>},
            {<record>},
            {<record>},
        ],
        u'num_results': 10,
        u'page': 1
    }
```

> We can edit the newly created `action_type` with a `PUT` request:

```python
    url = 'https://smartapi.bboxx.co.uk/v1/action_types/1'
    data = json.dumps({
		"name": "changed",
		"description": "changed",
		"label": "changed",
		})
    headers = {'Content-Type': 'application/json', 'Authorization': 'Token token=A_VALID_TOKEN'}

    r = requests.put(url=url, data=data, headers=headers)

    r
    >>> <Response 200>

    r.json()
    >>> {
		"action_type_id": 1
		"name": "changed",
		"description": "changed",
		"label": "changed",
		"created_at": "2000-01-01 00:00:00"
		"created_by": "test.user@bboxx.co.uk"
		"modified_at": 2016-07-07 12:34:45
	}
```
> Note that the `modified_at` field has been updated accordingly.

> If a user has `SYSTEM` permissions they can delete the `action_type`

```python
    url = 'https://smartapi.bboxx.co.uk/v1/action_types/1'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Token token=A_VALID_TOKEN'}

    r = requests.delete(url=url, headers=headers)

    r
    >>> <Response 204>

    r.text
    >>>
```
> Note that the response from a 204 request is empty. This means that `r.json()` cannot be called and will throw a JSONDecodeError. In fact the response is `u''` - an empty unicode string.



### POST
     | value
 ----:|:---
endpoint | `/v1/action_types`
method | `POST`
url_params | <font color="DarkGray">N/A</font>
query params | <font color="DarkGray">N/A</font>
body | JSON-formatted dictionary with the details of the `action_type` that you wish to create
permissions | <font color="Crimson">__`SYSTEM`__</font>
response | `201`

### GET
     | value
 ----:|:---
endpoint | `/v1/action_types` or `/v1/action_types/<action_type_id>`
method | `GET`
url_params | `action_type_id` <font color="DarkGray">_(int)_</font>
query params | *> See Query Format and Filtering*
body | <font color="DarkGray">N/A</font>
permissions | <font color="Jade">__`OVERVIEW`__</font>
response | `200`

### PUT
     | value
 ----:|:---
endpoint | `/v1/action_types/<action_type_id>`
method | `PUT`
url_params | `action_type_id` of the action_type you wish to edit
query params | <font color="DarkGray">N/A</font>
body | JSON-formatted dictionary of the columns that you wish to alter
permissions | <font color="Crimson">__`SYSTEM`__</font>
response | `200`

### DELETE
     | value
 ----:|:---
endpoint | `/v1/action_types/<action_type_id>`
method | `DELETE`
url_params | `action_type_id` <font color="DarkGray">_(int)_</font>
query params | <font color="DarkGray">N/A</font>
body | <font color="DarkGray">N/A</font>
permissions | <font color="Crimson">__`SYSTEM`__</font>
response | `204`

    
