# Ping

Ping the MelCtl API server.

## Usage

```shell
melctl ping [common args] [-s,--seconds SECONDS]
```

| Argument          | Required | Default | Description                        |
| ----------------- | -------- | ------- | ---------------------------------- |
| `-s`, `--seconds` | No       | `0`     | Background task time to completion |

## Example return

Table:

```
ping    apiVersion    serverVersion    taskId
------  ------------  ---------------  ------------------------------------
pong    v2            0.0.1            348bfa4f-30af-4e69-b020-cd23a41d2e15
```

YAML:

```yaml
apiVersion: v2
ping: pong
serverVersion: 0.0.1
taskId: 83460b10-9806-4b3d-ac3c-4739873abca7
```

---
