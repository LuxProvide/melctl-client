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

| Attribute                 | Type     | Default                                                                   | Description                   |
| ------------------------- | -------- | ------------------------------------------------------------------------- | ----------------------------- |
| `url`                     | `string` | `https://melctl.lxp-prod.cloud.lxp.lu`                                    | MelCtl API server URL         |
| `public_releases_api`     | `string` | `'https://api.github.com/repos/LuxProvide/melctl-client/releases/latest'` | Public release URL            |
| `public_releases_timeout` | `int`    | `0.5`                                                                     | Public update check timeout   |
| `public_releases_freq`    | `int`    | `60`                                                                      | Public update check frequency |

### Secrets

The secrets directory is located from:

* 1 - Environment variable `MELCTL_CLI_SECRETS`
* 2 - Directory `~/.melctl-secrets`

---
