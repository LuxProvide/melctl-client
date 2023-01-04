# Tasks

Run tasks, get their status and their results.

## Usage

```shell
melctl tasks {list,queued,status,get,submit} [common args]
```

### List defined tasks

```shell
melctl tasks list [common args]
```

### List queued tasks

```shell
melctl tasks queued [common args]
```

### Get a task status

```shell
melctl tasks status <task_id> [common args]
```

### Get a task result

```shell
melctl tasks get <task_id> [common args]
```

### Run a task

```shell
melctl tasks submit <name> [--args ARGS ...] [common args]
```

* `name` is a task name, as returned by `melctl tasks list`
* `--args` takes one or more argument
  * You may prefix an integer or float with `int:` or `float`, e.g. `--args foo bar int:42`

## Example return

To do.

---
