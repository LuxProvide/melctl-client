<!-- vim: set ft=2 ts=Markdown -->

# MelCtl - Client

The `melctl` command line interface.

\[TOC\]

## Installation

MelCtl client can be installed in 2 ways:

* From its Python package
* From source

### Python package

Requirements:
* `python3.8+`
* Python's module `pip`
* A GitLab PAT (_Personal Access Token_)

Command:

```shell
pip install --index-url https://__token__:<PAT>@gitlab.lxp.lu/api/v4/projects/179/packages/pypi/simple melctl-client
```

Notes:
* Replace `<PAT>` with your GitLab PAT (i.e. `glpat-a1b2c3d4...`)
* Do **not** replace `__token__`

### From source

Requirements:
* `python3.8+`
* `git`

Steps:
* (Optional) Create a virtual environment: `python3 -m venv <venv name>`
* (Optional) Activate the virtual environment: `source <venv path>/bin/activate`
* Clone this reposiory
* Install the client from witihn the repository: `pip install -e client/`

## Command line usage

General syntax:

```shell
melctl <endpoint> [action] [arguments]
```

* _endpoint_ refers to the API endpoint your're accessing, e.g, `tasks`
* _action_ refers to the action to perform (not all _endpoints_ have _actions_)
* _arguments_ refers to the endpoint's or endpoint's action's argument

### Login

See [the login documentation page](./docs/endpoints/login.md)

### Command examples

To get the list of available endpoints:

```shell
melctl -h
```

To get the list of an endpoint's actions (if any):

```shell
melctl <endpoint> -h
```

To get the list of an endpoint's actions arguments (if any):

```shell
melctl <endpoint> <action> -h
```

### Command arguments

Some arguments are common for most endpoints and endpoints's actions:

* `-h`, `--help`: Show the endpoint or endpoint's action help
* `-a AUTH`, `--auth AUTH`: Select the authentication token (e.g. `Bearer <JWT>`)
* `-u URL`, `--url URL`: Select the API server base URL (e.g. `http://host.tld:port`)
* `-v VERSION`, `--version VERSION`: Select the API endpoint version (e.g. `v1`)
* `-o FORMAT`, `--output-format FORMAT`: Select the command outpout format
  * `table` (default): Format output as table
  * `wide`: Format output as table with all available fields
  * `json`: Format output as JSON document
  * `yaml`: Format output as YAML document

### Endpoints

| Endpoint   | Action      | Description                            | Documentation                        |
| ---------- | ----------- | -------------------------------------- | ------------------------------------ |
| `ping`     | -           | Ping the MelCtl API server             | [Link](./docs/endpoints/ping.md)     |
| `version`  | -           | Print MelCtl client and server version | [Link](./docs/endpoints/version.md)  |
| `config`   | `show`      | Show the client configuration          | [Link](./docs/endpoints/config.md)   |
| `config`   | `init`      | Initialize a new default configuration | [Link](./docs/endpoints/config.md)   |
| `login`    | `user`      | Login / get an user token              | [Link](./docs/endpoints/login.md)    |
| `login`    | `admin`     | Login / get an admin token             | [Link](./docs/endpoints/login.md)    |
| `login`    | `info`      | Get login / token information          | [Link](./docs/endpoints/login.md)    |
| `curl`     | -           | Performs low-level API call            | [Link](./docs/endpoints/curl.md)     |
| `tasks`    | `list`      | List available tasks                   | [Link](./docs/endpoints/tasks.md)    |
| `tasks`    | `queued`    | List queued and running tasks          | [Link](./docs/endpoints/tasks.md)    |
| `tasks`    | `status`    | Get a task status                      | [Link](./docs/endpoints/tasks.md)    |
| `tasks`    | `get`       | Get a task result                      | [Link](./docs/endpoints/tasks.md)    |
| `tasks`    | `submit`    | Runs a new task                        | [Link](./docs/endpoints/tasks.md)    |
| `projects` | `list`      | List all projects                      | [Link](./docs/endpoints/projects.md) |
| `projects` | `get`       | Get one or more project information    | [Link](./docs/endpoints/projects.md) |
| `projects` | `report`    | Reports one or all projects usage      | [Link](./docs/endpoints/projects.md) |
| `users`    | `list`      | List users                             | [Link](./docs/endpoints/users.md)    |
| `users`    | `get`       | Get a specific user                    | [Link](./docs/endpoints/users.md)    |
| `users`    | `s3-status` | Get an user S3 access                  | [Link](./docs/endpoints/users.md)    |
| `users`    | `s3-setup`  | Setup an user S3 access                | [Link](./docs/endpoints/users.md)    |
| `s3ds`     | `list`      | List S3 access keys                    | [Link](./docs/endpoints/s3ds.md)     |
| `s3ds`     | `setup`     | Create and configure S3 accesses keys  | [Link](./docs/endpoints/s3ds.md)     |
| `s3ds`     | `disable`   | Disable S3 accesses keys               | [Link](./docs/endpoints/s3ds.md)     |

### JQ scripting

`jq` parses and filters JSON document. MelCtl can be piped into `jq`:

```shell
melctl <endpoint> [action] [arguments] --nocolor -o json 2>/dev/null | jq [filter]
```

Where:
* `--nocolor` disable MelCtl colored output
* `-o json` renders MelCtl output as JSON
* `filter` is the JQ filter(s) to apply

#### Render output using JQ

```shell
melctl users list --nocolor -o json 2>/dev/null | jq 
```

#### Using JQ on list of objects

If MelCtl JSON output is a list of object like:

```json
[
    {
        "name": "jpclipffel",
        "uid": 15019,
        "s3ds": {
            "tag": "jpclipffel",
            "fspaths": "/mnt/tier2/users/jpclipffel"
        }
    },
    {
        "name": "foo",
        "uid": 12345,
        "s3ds": {}
    },
    // ...
]
```

Use filters like this:

```shell
# Select all objects name
... | jq '.[].name'

# Select all objects with S3DS content
... | jq '.[] | select((.s3ds | length) > 0)'
```

## Python API usage

> **Note**  
> Python API is currently a second-class citizen.  

General usage (can be run from an `ipython` instance):

```python
import melctl_client.__main__

# Create a blocking and a non-blocking API instances
api_sync = melctl_client.__main__.API()
api_async = melctl_client.__main__.API(blocking=False)

# Run
ping_data = api_sync('ping')
projects_data = api_async('projects', 'get', 'lxp')

# Output sync response
# ping_data = {'ping': 'pong', 'serverVersion': 'x.y.z', ...}
print(ping_data)

# Output async response
# projects_data = {'taskId': '80282886-a3b1-4443-8f0b-69e120e0844d'}
print(projects_data)
```

## Configuration

By default, `melctl` will use the cofiguration file `~/.melctl-cli.env`. You may
change the configration file location by setting the environement
variable `MELCTL_CLI_CONFIG`:

```
MELCTL_CLI_CONFIG="/etc/melctl-cli.env" melctl <endpoint> [action] [arguments]
```

The following configuration attributes are supported:

| Attribute | Type     | Default                 | Description           |
| --------- | -------- | ----------------------- | --------------------- |
| `url`     | `string` | `http://127.0.0.1:8888` | MelCtl API server URL |

## Developers documentation

### Add endpoint(s)

Endpoints are defined in `client/melctl_client/endpoints/<module.py>`, and
should be registered in `client/melctl_client/endpoints/__init__.py`.

Let's start by creating a `SimpleEndpoint`, e.g. `test.py` in
`client/melctl_client/endpoints/test.py`:

```python
from .__base__ import SimpleEndpoint


class Ping(SimpleEndpoint):
    """Demonstrates MelCtl endpoint.
    """

    def __init__(self, subparser):
        """Initializes the endpoint.

        This SimpleEndpoint initialize its parent class with:
            - subparser: The command line parser
            - ``test``: The endpoint action name
            - ``GET``: The HTTP method to invoke
            - ``test/ping?data={data}``: The URL fragment to template and invoke
        """
        super().__init__(subparser, 'ping', 'GET', 'test/ping?data={data}')
        self.parser.add_argument('-d', '--data', dest='data', type=str,
            default=None, help='Test ping data')
```

For more complex use cases, you may implement an `Endpoint` instead of
a `SimpleEndpoint`:

```python
from .__base__ import Endpoint


class Callback(Endpoint):
    """Demonstrates MelCtl callback endpoint.
    """

    hint_callback_url: str = '<MelCtl host>/test/callback/receive'

    def __init__(self, subparser):
        """Initializes the endpoint.

        This Endpoint initialize its parent class with:
            - subparser: The command line parser
            - ``callback``: The endpoint action name
        """
        super().__init__(subparser, 'callback')
        self.parser.add_argument('cback_url', type=str,
            help=f'Callback URL (you may try "{self.hint_callback_url}")')
        self.parser.add_argument('-m', '--method', dest='method', type=str.upper,
            default='POST', help='Callback HTTP method')

    def target(self, args):
        """Runs the endpoint.

        An ``Endpoint`` must implement a ``target`` method to call the API server.
        Parsed arguments are made available in ``args``.
        """
        req = self.session.get(
            f'{self.url}/test/callback/send'
            f'?url={args.cback_url}'
            f'&method={args.method}'
        )
        req.raise_for_status()
        return req.json()
```

You may also define the method `render` to post-process the API result:

```python
class MyEndpoint(Endpoint):

    # ...

    def render(self, args, data):
        """Change the API return (i.e. ``data``).
        """
        return data.get('someField', 42)
```

When your new endpoint(s) are ready to be exposed, you have to `import`
(==register) them in `client/melctl_client/endpoints/__init__.py`:

```python
# Import the endpoint module(s)
from . import ping
from . import test
# ...

# Register the endpoints
endpoints = {
    # If the endpoint has a single action, use it directly
    'ping': ping.Ping,
    # If the endpoint implement multiples actions, use a list
    'test': [
        test.Ping,
        test.Callback
    ],
    # ...
}
```
