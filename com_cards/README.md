# Tag Registry Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all Tags

**Definition**:

`GET /tags`

**Response**:

- `200 OK` on success

```json
[
    {
        "identifier": "squid-ink",
        "name": "Inky Blackness",
        "character": "Benji",
        "description": "The Kraken can deploy a cloud of inky blackness that floats in midair",
        "max_use":"3",
        "current_use":"0"
    },
    {
        "identifier": "shadow-dog",
        "name": "Faithful Hound",
        "character": "Bernie",
        "description": "A shadowy dog that protects either the user, or the person the user is focussing on",
        "max_use":3,
        "current_use":0
    }
]
```

### Registering a new Tag

**Definition**:

`POST /tags`

**Arguments**:

- `"identifier":string` a globally unique identifier for this tag
- `"name":string` a friendly name for this tag
- `"character":string` which character uses this tag
- `"description":string` a general description of the tag
- `"max_use":int` how many times the tag can be used before it's burned
- `"current_use":int` how many times the tag has been used

If a Tag with the given identifier already exists, the existing Tag will be overwritten.

**Response**:

- `201 Created` on success

```json
{
    "identifier": "shadow-dog",
        "name": "Faithful Hound",
        "character": "Bernie",
        "description": "A shadowy dog that protects either the user, or the person the user is focussing on",
        "max_use":3,
        "current_use":0
}
```

## Lookup Tag details

`GET /tag/<identifier>`

**Response**:

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{
    "identifier": "shadow-dog",
        "name": "Faithful Hound",
        "character": "Bernie",
        "description": "A shadowy dog that protects either the user, or the person the user is focussing on",
        "max_use":3,
        "current_use":0
}
```

## Delete a Tag

**Definition**:

`DELETE /tag/<identifier>`

**Response**:

- `404 Not Found` if the device does not exist
- `204 No Content` on success

## Update Tag

**Definition**:

`PUT/tag/<identifier>`

**Arguments**:
-`"current_use":int` the updated current use value

**Response**:

- `404 Not Found` if the device does not exist
- `200 OK` on success
