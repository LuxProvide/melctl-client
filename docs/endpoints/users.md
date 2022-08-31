# MelCtl - Client - Users

Manage MeluXina users.

## Usage

```shell
melctl users {list,get,s3-status,s3-setup} [common args]
```

### List all users

```shell
melctl users list [common args]
```

Example return as table (truncated):

```
name                      uid         gid  preserved    expired
-----------------  ----------  ----------  -----------  ---------
admin              1036800000  1036800000  False        False
ahacar                  15015         555  False        False
app-argocd         1036800072  1036800072  False        False
app-jupyter        1036800071  1036800071  False        False
app-melctl         1036800058         555  False        False
jpclipffel              15019         555  False        False
```

Example return as YAML (truncated):

```yaml
- expired: false
  gid: 555
  groups:
  - admins
  - ipausers
  - lxp_ops
  - lxp
  - grp-openstack-admins
  - grp-cgw
  - vpn
  - grp-openstack
  - grp-ipam
  - grp-melctl-admins
  - grp-rundeck-admin
  - grp-argocd-admins
  name: jpclipffel
  preserved: false
  s3ds:
    current_usage: 0
    enabled: true
    fspaths: /mnt/tier2/users/jpclipffel
    fsuid: 15019:555
    quotalimit: UNLIMITED
    tag: jpclipffel
    uuid: 1337c6de830200667ef2c5c16c9959c1c03d2405
  uid: 15019
```

### Get a user information

```shell
melctl users get <name> [common args]
```

* `name` is a user name as appearing in the IDM.

Example return as table:

```
name          uid    gid  preserved    expired
----------  -----  -----  -----------  ---------
jpclipffel  15019    555  False        False
```

Example return as YAML:

```yaml
- expired: false
  gid: 555
  groups:
  - grp-rundeck-admin
  - grp-melctl-admins
  - grp-argocd-admins
  - vpn
  - ipausers
  - grp-openstack
  - grp-ipam
  - lxp_ops
  - admins
  - lxp
  - grp-openstack-admins
  - grp-cgw
  name: jpclipffel
  preserved: false
  s3ds:
    current_usage: 0
    enabled: true
    fspaths: /mnt/tier2/users/jpclipffel
    fsuid: 15019:555
    quotalimit: UNLIMITED
    tag: jpclipffel
    uuid: 1337c6de830200667ef2c5c16c9959c1c03d2405
  uid: 15019
```

---
