# S3DS

Manage S3DS.

## Usage

```shell
melctl s3ds {list,setup,disable} [common args]
```

### List access keys

```shell
melctl s3ds list [common args]
```

Example return as table (truncated):

```
tag               uuid
----------------  ----------------------------------------
scortet           0fcbfcd1a94d151dc82d37aa25d62c7799082458
(reserved)        74e3cbde7aeaa539b3233e29d25b1d304ca514d0
(reserved)        43a28c7c67f94b768328a587b218f0e6d17f89fb
jpclipffel        1337c6de830200667ef2c5c16c9959c1c03d2405
rderooy           3a3e7debbc9be3b4525e8683f0e829399da6017b
ADMIN (reserved)  No UUID for ADMIN
(reserved)        aecf16047b706024a0505c83e9933df6096000dc
```

Example return as YAML (truncated):

```yaml
- accesskey: "****"
  current_usage: 0
  enabled: true
  fspaths: /mnt/tier2/users/jpclipffel
  fsuid: 15019:555
  quotalimit: UNLIMITED
  secretkey: "****"
  tag: jpclipffel
  uuid: 1337c6de830200667ef2c5c16c9959c1c03d2405
```

### Create an access key

> **Warning**  
> One **should really** use the `users` endpoint to create an user access key.  
> See [the endpoint documentation](./users.md)  

```
melctl s3ds setup <username> --uid <uid> --gid <gid> --paths <path> [path, ...]
```

Example return as table:

```
s3ds_status
---------------------------------------------------
{'strategy': 'create', 'code': 200, 'reason': 'OK'}
```

---
