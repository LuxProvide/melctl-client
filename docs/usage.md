<!-- vim: set ft=4 ts=Markdown -->

# Usage

## General syntax

```shell
melctl <command> [action] [arguments]
```

Where:

* `command` refers to the API endpoint you're accessing, e.g, `projects`
    * Each plugin may implement one or more `command`
* `action` refers to the action to perform (not every `command` has _actions_)
* `arguments` refers to the command's or command's action's argument

## Commands syntax

Get the list of available commands:

```shell
melctl -h
```

Get the list of a command's actions (if any):

```shell
melctl <command> -h
```

Get the list of a command's actions arguments (if any):

```shell
melctl <command> <action> -h
```

## Common arguments

Some arguments are common to most commands and command's actions:

* `-h`, `--help`: Show the endpoint or endpoint's action help
* `-a AUTH`, `--auth AUTH`: Select the authentication token (e.g. `Bearer <JWT>`)
* `-u URL`, `--url URL`: Select the API server base URL (e.g. `http://host.tld:port`)
* `-v VERSION`, `--version VERSION`: Select the API endpoint version (e.g. `v1`)
* `-o FORMAT`, `--output-format FORMAT`: Select the command output format
    * `table`: Format output as table
    * `wide`: Format output as table with all available fields
    * `json`: Format output as JSON document
    * `yaml`: Format output as YAML document

## JQ scripting

`jq` parses and filters JSON documents. MelCtl can be piped into `jq`:

```shell
melctl <command> [action] [arguments] --nocolor -o json 2>/dev/null | jq <script>
```

Where:

* `--nocolor` disable MelCtl colored output
* `-o json` renders MelCtl output as JSON
* `script` is the JQ script to apply

### Render output using JQ

```shell
melctl users list --nocolor -o json 2>/dev/null | jq 
```

### Using JQ on a list of objects

If MelCtl JSON output is a list of objects like:

```json
[
    {
        "name": "jpclipffel",
        "uid": 15019,
        "s3ds": {
            "tag": "jpclipffel",
            "fspaths": "/mnt/tier2/users/jpclipffel"
        }
    },
    {
        "name": "foo",
        "uid": 12345,
        "s3ds": {}
    },
    // ...
]
```

Use filters like this:

```shell
# Select all objects name
... | jq '.[].name'

# Filer empty values
... | jq '.[] | select(.email != null) | select(.email | match("jpclipffel"))'

# Select all objects with S3DS content
... | jq '.[] | select((.s3ds | length) > 0)'
```
