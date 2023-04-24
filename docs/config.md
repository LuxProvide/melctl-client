# Configuration

The `melctl` client can be configured via command line arguments and via a
configuration file.

## Initial configuration

After the first installation, run `melctl config init` to initialize the configuration file:

```shell
melctl config init
```

!!! note "Internal users"
    Internal users should change the MelCTL server URL to point to the internal production instance.

    Edit the environment file `melctl-cli.env` (you may find the full path using `melctl config show`)
    and change the URL parameter (`url="https://melctl..."`) to the appropriate value.

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
