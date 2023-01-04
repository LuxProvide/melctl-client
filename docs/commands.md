# Commands reference

## Builtins

| Command   | Action | Description                            | Documentation                         |
| --------- | ------ | -------------------------------------- | ------------------------------------- |
| `ping`    | -      | Ping the MelCtl API server             | [Link](./plugins/builtins/ping.md)    |
| `version` | -      | Print MelCtl client and server version | [Link](./plugins/builtins/version.md) |
| `config`  | `show` | Show the client configuration          | [Link](./plugins/builtins/config.md)  |
| `config`  | `init` | Initialize a new default configuration | [Link](./plugins/builtins/config.md)  |

## Customer

| Command   | Action | Description                            | Documentation                         |
| --------- | ------ | -------------------------------------- | ------------------------------------- |

## Admin

| Command    | Action         | Description                           | Documentation                       |
| ---------- | -------------- | ------------------------------------- | ----------------------------------- |
| `curl`     | -              | Performs low-level API call           | [Link](./plugins/admin/curl.md)     |
| `login`    | `user`         | Login / get an user token             | [Link](./plugins/admin/login.md)    |
| `login`    | `admin`        | Login / get an admin token            | [Link](./plugins/admin/login.md)    |
| `login`    | `info`         | Get login / token information         | [Link](./plugins/admin/login.md)    |
| `projects` | `list`         | List all projects                     | [Link](./plugins/admin/projects.md) |
| `projects` | `get`          | Get one or more project information   | [Link](./plugins/admin/projects.md) |
| `projects` | `create`       | Create a project                      | [Link](./plugins/admin/projects.md) |
| `projects` | `report`       | Reports one or all projects usage     | [Link](./plugins/admin/projects.md) |
| `projects` | `add-user`     | Add users to a project                | [Link](./plugins/admin/projects.md) |
| `projects` | `add-coord`    | Add coordinators to a project         | [Link](./plugins/admin/projects.md) |
| `projects` | `del-user`     | Remove users from a project           | [Link](./plugins/admin/projects.md) |
| `projects` | `del-coord`    | Remove coordinators from a project    | [Link](./plugins/admin/projects.md) |
| `projects` | `add-sharedfs` | Add a shared fs tier to a project     | [Link](./plugins/admin/projects.md) |
| `projects` | `set-quotas`   | Set a project quotas                  | [Link](./plugins/admin/projects.md) |
| `s3ds`     | `list`         | List S3 access keys                   | [Link](./plugins/admin/s3ds.md)     |
| `s3ds`     | `setup`        | Create and configure S3 accesses keys | [Link](./plugins/admin/s3ds.md)     |
| `s3ds`     | `disable`      | Disable S3 accesses keys              | [Link](./plugins/admin/s3ds.md)     |
| `tasks`    | `list`         | List available tasks                  | [Link](./plugins/admin/tasks.md)    |
| `tasks`    | `queued`       | List queued and running tasks         | [Link](./plugins/admin/tasks.md)    |
| `tasks`    | `status`       | Get a task status                     | [Link](./plugins/admin/tasks.md)    |
| `tasks`    | `get`          | Get a task result                     | [Link](./plugins/admin/tasks.md)    |
| `tasks`    | `submit`       | Runs a new task                       | [Link](./plugins/admin/tasks.md)    |
| `users`    | `list`         | List users                            | [Link](./plugins/admin/users.md)    |
| `users`    | `get`          | Get a specific user                   | [Link](./plugins/admin/users.md)    |
| `users`    | `create`       | Create an user                        | [Link](./plugins/admin/users.md)    |
| `users`    | `s3-status`    | Get an user S3 access                 | [Link](./plugins/admin/users.md)    |
| `users`    | `s3-setup`     | Setup an user S3 access               | [Link](./plugins/admin/users.md)    |

---
