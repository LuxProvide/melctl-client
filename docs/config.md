# Configuration

The `melctl` client can be configured via command line arguments and via a
configuration file.

## Configurable items

| Argument       | Config key   | Description                     |
| -------------- | ------------ | ------------------------------- |
| `-a`, `--auth` | `auth_token` | API server authentication token |
| `-u`, `--url`  | `url`        | API server URL                  |

## Configuration sources

MelCTL client has two configuration sources:

* The configuration file (stores configuration variables)
* The secrets directory (stores tokens)

You can generate the configuration assets using `melctl config init`.
See [plugins/builtins/config](./plugins/builtins/config.md)

If no configuration is found, `melctl` will complain when invoked.

### Configuration file

The configuration file is located from:

* 1 - Environment variable `MELCTL_CLI_CONFIG`
* 2 - File `~/.melctl-cli.env`

The following configuration attributes are supported:

| Attribute | Type     | Default                 | Description           |
| --------- | -------- | ----------------------- | --------------------- |
| `url`     | `string` | `http://127.0.0.1:8888` | MelCtl API server URL |

### Secrets

The secrets directory is located from:

* 1 - Environment variable `MELCTL_CLI_SECRETS`
* 2 - Directory `~/.melctl-secrets`

---
