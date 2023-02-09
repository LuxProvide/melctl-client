# Tasks

Run tasks, get their status and their results.

## Usage

```shell
melctl tasks {list,queued,status,get,submit} [arguments]
```

### List defined tasks

```shell
melctl tasks list [arguments]
```

### List queued tasks

```shell
melctl tasks queued [arguments]
```

### Get a task status

```shell
melctl tasks status <task_id> [arguments]
```

### Get a task result

```shell
melctl tasks get <task_id> [arguments]
```

### Run a task

```shell
melctl tasks submit <name> [--args ARGS...] [--kwargs '{...}'] [arguments]
```

* `name` is a task name, as returned by `melctl tasks list`
* `--args` takes one or more argument
    * You may prefix an integer or float with `int:` or `float`, e.g. `--args foo bar int:42`
* `--kwargs` takes a JSON string as sole argument
    * Arguments type are inferred using standard JSON types
    * Example: `--kwargs '{"name": "foo", "value": 42}'`

## Example return

To do.

---
