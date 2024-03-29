<!-- vim: set ft=4 ts=Markdown -->

# Installation and upgrade

MelCtl and its plugins may be installed and upgraded either from their Python
packages using `pip` or from source.

## Notes

* MelCtl and its plugins may optionally be installed in a virtual environment:
    * Create a virtual environment: `python3 -m venv <venv name>`
    * Activate the virtual environment: `source <venv path>/bin/activate`
* If you are frequently updating MelCtl, you may install it in _editable mode_ (`pip install -e ...`)

## LuxProvide customers

### Requirements

* Python 3.8 or newer
* Python's `pip`
* Git client (when installing or upgrading from source)

### Installation from the Python package

Install `melctl-client` and the plugins:

```shell
pip3 install melctl-client melctl-client-plugins-customer
```

Upgrade `melctl-client` and the plugins:

```
pip3 install --upgrade melctl-client melctl-client-plugins-customer
```

### Installation from source

Clone the public repositories:

```shell
git clone https://github.com/LuxProvide/melctl-client
git clone https://github.com/LuxProvide/melctl-client-plugins-customer
```

Install `melctl-client` and the plugins:

```shell
pip3 install ./melctl-client ./melctl-client-plugins-customer
```

### Upgrade from source

Update `melctl-client` and the sources of the plugins:

```shell
git pull melctl-client
git pull melctl-client-plugins-customer
```

Upgrade `melctl-client` and the plugins:

```shell
pip3 install --upgrade ./melctl-client ./melctl-client-plugins-customer
```

---

## Internal users

### Requirements

* Python 3.8 or newer
* Python's `pip`
* Git client (when installing or upgrading from source)
* GitLab PAT (_Personal Access Token_), further referred as `<PAT>`  
    In the next examples:
    * Replace `<PAT>` with your GitLab PAT (i.e. `glpat-a1b2c3d4...`)
    * Do **not** replace `__token__`

### Installation from the Python package

Install `melctl-client`:

```shell
pip3 install --index-url https://__token__:<PAT>@gitlab.lxp.lu/api/v4/projects/179/packages/pypi/simple melctl-client
```

Install the admin plugins:

```shell
pip3 install --index-url https://__token__:<PAT>@gitlab.lxp.lu/api/v4/projects/179/packages/pypi/simple melctl-client-plugins-admin
```

Install the customer plugins:

```shell
pip3 install --index-url https://__token__:<PAT>@gitlab.lxp.lu/api/v4/projects/179/packages/pypi/simple melctl-client-plugins-customer
```

### Installation from source

Clone the internal repositories:

```shell
git clone ssh://git@gitlab.lxp.lu:8822/lxp-hpc/IaC/meluxina/melctl-client
git clone ssh://git@gitlab.lxp.lu:8822/lxp-hpc/IaC/meluxina/melctl-client-plugins/admin melctl-client-plugins-admin
git clone ssh://git@gitlab.lxp.lu:8822/lxp-hpc/IaC/meluxina/melctl-client-plugins/customer melctl-client-plugins-customer
```

Install `melctl-client` and the plugins:

```shell
pip3 install ./melctl-client ./melctl-client-plugins-admin ./melctl-client-plugins-customer
```

### Upgrade from source

Update `melctl-client` and the sources of the plugins:

```shell
git -C melctl-client pull
git -C melctl-client-plugins-admin pull
git -C melctl-client-plugins-customer pull
```

Upgrade `melctl-client` and the plugins:

```shell
pip3 install --upgrade ./melctl-client ./melctl-client-plugins-admin ./melctl-client-plugins-customer
```

---
