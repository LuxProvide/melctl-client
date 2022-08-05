# MelCtl - Client - Config

The `melctl` client can be configured via command line arguments and via a
configuration file.

| Argument       | Config key   | Description                     |
| -------------- | ------------ | ------------------------------- |
| `-a`, `--auth` | `auth_token` | API server authentication token |
| `-u`, `--url`  | `url`        | API server URL                  |

## Configuration sources

MelCTL client has two configuration sources:

* The configuration file (stores configuration variables)
* The secrets directory (stores tokens)

You can generate the configuration assets using `melctl config init`.
See [endpoint/config.md](./endpoints/config.md)

If no configuration is found, `melctl` will complain when invoked.

### Configuration file

The configuration file is located from:

* 1 - Environment varibale `MELCTL_CLI_CONFIG`
* 2 - File `~/.melctl-cli.env`

### Secrets

The secrets directory is located from:

* 1 - Environment varibale `MELCTL_CLI_SECRETS`
* 2 - Directory `~/.melctl-secrets`

---
