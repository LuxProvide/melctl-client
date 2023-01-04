<!-- vim: set ft=4 ts=Markdown -->


# Plugins

## Plugin structure

Example with a plugin called `foobar`:

```shell
.
├── melctl_client_plugins
│   └── foobar
│       ├── __init__.py
│       ├── foo.py
│       └── bar.py
└── setup.py
```

Where:

* `.` is the plugin root project / repository
* `melctl_client_plugins` is the _namespace package_ which contains the plugin code
* `foobar` is the plugin source directory
* `__init__.py` exposes the plugin _commands_
* `foo.py` and `bar.py` implements the plugin _commands_
* `setup.py` is the plugin installation script

## Installation script -  `setup.py`

Example:

```python
from setuptools import setup, find_namespace_packages


setup(
    name='melctl_client_plugins_foobar',
    packages=find_namespace_packages(include=['melctl_client_plugins.*']),
    install_requires=[
        'melctl_client',
    ]
)
```

## Commands implementation

See [commands.md](./commands.md)

---
