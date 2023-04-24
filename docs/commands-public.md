# Commands reference

## Builtins

<!-- Keep it synced with commands-public.md -->
| Command    | Action | Description                             | Documentation                          |
| ---------- | ------ | --------------------------------------- | -------------------------------------- |
| `ping`     | -      | Ping the MelCtl API server              | [Link](./plugins/builtins/ping.md)     |
| `login`    | `user` | Login / get an user token               | [Link](./plugins/builtins/login.md)    |
| `login`    | `info` | Get login / token information           | [Link](./plugins/builtins/login.md)    |
| `config`   | `show` | Show the client configuration           | [Link](./plugins/builtins/config.md)   |
| `config`   | `init` | Initialize a new default configuration  | [Link](./plugins/builtins/config.md)   |
| `complete` | `bash` | Generate the Bash autocompletion script | [Link](./plugins/builtins/complete.md) |
| `complete` | `zsh`  | Generate the ZSH autocompletion script  | [Link](./plugins/builtins/complete.md) |
| `version`  | -      | Print MelCtl client and server version  | [Link](./plugins/builtins/version.md)  |

## Customer

<!-- Keep it synced with commands.md -->
| Command | Action    | Description                             | Documentation                    |
| ------- | --------- | --------------------------------------- | -------------------------------- |
| `s3`    | `login`   | Login to LuxProvide S3 gateway          | [Link](./plugins/customer/s3.md) |
| `s3`    | `logout`  | Logout from LuxProvide S3 gateway       | [Link](./plugins/customer/s3.md) |
| `s3`    | `info`    | Get S3 account information              | [Link](./plugins/customer/s3.md) |
| `s3`    | `ls`      | List S3 buckets and bucket's contents   | [Link](./plugins/customer/s3.md) |
| `s3`    | `mb`      | Create S3 bucket                        | [Link](./plugins/customer/s3.md) |
| `s3`    | `rb`      | Delete S3 bucket                        | [Link](./plugins/customer/s3.md) |
| `s3`    | `del`     | Delete S3 bucket content                | [Link](./plugins/customer/s3.md) |
| `s3`    | `cp`      | Copy data from/to bucket                | [Link](./plugins/customer/s3.md) |
| `s3`    | `genconf` | Generate other S3 clients configuration | [Link](./plugins/customer/s3.md) |

---
