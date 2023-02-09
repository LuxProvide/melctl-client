# Config

Show and generate the `melctl` client configuration.

## Usage

```shell
melctl config {show,init} [common args]
```

### `show` - Show current configuration

```shell
melctl config show [common args]
```

```
url                    token    env_file                          secrets_dir
---------------------  -------  --------------------------------  --------------------------------
http://127.0.0.1:8888  *******  /home/jpclipffel/.melctl-cli.env  /home/jpclipffel/.melctl-secrets
```

### `init` - Generate a new configuration

```shell
melctl config init [common args]
```

This command will generate:

* A new configuration file with default values
* A new directory to hold MelCtl secrets

The existing configuration **is not** replaced.

```
path                              status
--------------------------------  -----------------
/home/jpclipffel/.melctl-cli.env  File created
/home/jpclipffel/.melctl-secrets  Directory created
```

---
