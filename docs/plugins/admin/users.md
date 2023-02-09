# Users

Manage MeluXina users.

## Usage

```shell
melctl users {list,get,create,s3-status,s3-setup,s3-disable} [arguments]
```

### `list` - List all users

```shell
melctl users list [arguments]
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

### `get` - Get a user information

```shell
melctl users get <name> [arguments]
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

### `create` - Create an user

```shell
melctl users create \
    --email MAIL --firstname FIRSTNAME --lastname LASTNAME \
    [--name NAME --uid UID --gid GID] \
    [--phone PHONE]
```

Example to create a _customer_ new user (UID will be generated automatically):

```shell
melctl users create --email 'john.doe@fbi.gov.us' --firstname 'John' --lastname 'Doe' --phone '+0011223344'
```

Example to create a new _internal_ user:

```shell
melctl users create \
    --email 'john.doe@fbi.gov.us' --firstname 'John' --lastname 'Doe' \
    --name 'jdoe' --uid 15000 --gid 555
```

### `s3-status` - Get an user S3 status

```shell
melctl users s3-status <name> [arguments]
```

* `name` is a user name as appearing in the IDM.

Example return as table:

```
tag         uuid                                      fspaths                      fsuid
----------  ----------------------------------------  ---------------------------  ---------
jpclipffel  1337c6de830200667ef2c5c16c9959c1c03d2405  /mnt/tier2/users/jpclipffel  15019:555
```

Example return as YAML:

```yaml
- current_usage: 0
  enabled: true
  fspaths: /mnt/tier2/users/jpclipffel
  fsuid: 15019:555
  quotalimit: UNLIMITED
  tag: jpclipffel
  uuid: 1337c6de830200667ef2c5c16c9959c1c03d2405
```

### `s3-setup` Set user S3 access

```shell
melctl users s3-setup <name> [--paths <path>, ...]
```

* `name` is a user name as appearing in the IDM.
* `path` are extra path to allow

!!! warning "Secrets visibility"
    The S3 `secretkey` and `accesskey` are displayed only when the access is configured for the
    first time or when the access is re-enabled.

Example return as table:

```
tag         uuid                                      fspaths                      fsuid      secretkey    accesskey
----------  ----------------------------------------  ---------------------------  ---------  -----------  -----------
jpclipffel  1337c6de830200667ef2c5c16c9959c1c03d2405  /mnt/tier2/users/jpclipffel  15019:555  
```

Example return as YAML:

```yaml
- current_usage: 0
  enabled: true
  fspaths: /mnt/tier2/users/jpclipffel
  fsuid: 15019:555
  quotalimit: UNLIMITED
  tag: jpclipffel
  uuid: 1337c6de830200667ef2c5c16c9959c1c03d2405
  secretkey: null
  accesskey: null
```

---
