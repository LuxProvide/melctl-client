# Plugins

MelCtl _plugins_ implements client _commands_ and typically interfaces with one
or more API server _endpoints_.

| Plugin     | Description             | Repositories                                                              |
| ---------- | ----------------------- | ------------------------------------------------------------------------- |
| `builtins` | Built-in plugin         | -                                                                         |
| `customer` | Customer commands       | [Public][plugins-customer-public] / [Internal][plugins-customer-internal] |
| `admin`    | Administrative commands | [Internal][plugins-admin-internal]                                        |

---

[plugins-customer-public]: https://github.com/LuxProvide/melctl-client-plugins-customer
[plugins-customer-internal]: https://gitlab.lxp.lu/lxp-hpc/IaC/meluxina/melctl-client-plugins/customer
[plugins-admin-internal]: https://gitlab.lxp.lu/lxp-hpc/IaC/meluxina/melctl-client-plugins/admin
