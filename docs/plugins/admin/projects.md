# Projects

Manage MeluXina projects.

## Usage

```shell
melctl projects {list,get,create,report,add-user,add-coord,del-user,del-coord,add-sharedfs,set-quotas} [common args]
```

### `list` - List all projects

```shell
melctl projects list [common args]
```

Example return as table (truncated):

```
name       path
---------  -----------------------------
billtest   root.luxembourg.lxp.billtest
billtest2  root.luxembourg.lxp.billtest2
melsupp    root.luxembourg.melsupp
```

Example return as YAML (truncated):

```yaml
- children: {}
  coordinators:
  - app-melctl
  - jpclipffel
  - omula
  - ...
  name: melsupp
  path: root.luxembourg.melsupp
  users:
  - cthomaz
  - ...
```

### `get` - Get a project

```shell
melctl projects get <name> [common args]
```

* `name` is a project name as returned by `melctl projects list`

Example return as table (truncated):

```
name       users                 coordinators         children    path
---------  --------------------  -------------------  ----------  -----------------------------
billtest   ['wmainassara', ...]  ['app-melctl', ...]  {}          root.luxembourg.lxp.billtest
billtest2  ['mdenou', ...]       ['app-melctl', ...]  {}          root.luxembourg.lxp.billtest2
```

Example return as YAML (truncated):

```yaml
- children: {}
  coordinators:
  - app-melctl
  - ...
  name: billtest
  path: root.luxembourg.lxp.billtest
  users:
  - wmainassara
  - vplugaru
  - ...
- children: {}
  coordinators:
  - app-melctl
  - jpclipffel
  - ...
  name: billtest2
  path: root.luxembourg.lxp.billtest2
  users:
  - mdenou
  - ...
```

### `create` - Create a project

```shell
melctl projects create -p,--parent PARENT [[--name NAME] [--uid UID]]
```

Example to create a new EuroHPC project (name and UID are automatically generated):

```shell
melctl projects create -p eurohpc
```

Example to create a new Luxembourg project (name and UID are automatically generated):

```shell
melctl projects create -p luxembourg
```

Example to create a custom project with UID/GID `200999` named `lxp200999`:

```shell
melctl projects create -p lxp --uid 200999 --name lxp200999
```

### `report` - Get projects resource usage

```shell
melctl projects report [name] \
    [-r,--rangetime lastmonth] \
    [-s,--starttime TIME_START] \
    [-e,--endtime TIME_END] \
    [--time-unit s,sec,secs,second,seconds,m,min,mins,minute,minutes,h,hrs,hour,hours]
```

Example query for previous month usage:

```shell
melctl projects report -r lastmonth --time-unit hours
```

Example query for April 2002:

```shell
melctl projects report -s "2022-04-01" -e "2022-05-01" --time-unit hours
```

Example return as table (truncated):

```
name      disk        cpu      gpu    mem    fpga
--------  ------  -------  -------  -----  ------
lxp               3180816  2696785   6444  173387
billtest              112        0      0       0
melsupp              1905        0      0       0
```

Example return as YAML (truncated):

```yaml
- cpu: 3180930
  fpga: 173387
  gpu: 2696975
  mem: 6444
  name: lxp
- cpu: 112
  fpga: 0
  gpu: 0
  mem: 0
  name: billtest
- cpu: 1905
  fpga: 0
  gpu: 0
  mem: 0
  name: melsupp
```

### `add-user` - Add users to a project

```shell
melctl projects add-user PROJECT -m USER [USER ...]
```

Example to add users `u100001` and `u100002` to project `p200001`:

```shell
melctl projects add-user p200001 -m u100001 u100002
```

### `add-coord` - Add coordinators to a project

```shell
melctl projects add-coord PROJECT -m USER [USER ...]
```

Example to add coordinators `u100001` and `u100002` to project `p200001`:

```shell
melctl projects add-coord p200001 -m u100001 u100002
```

### `del-user` - Remove users from a project

```shell
melctl projects del-user PROJECT -m USER [USER ...]
```

Example to remove users `u100001` and `u100002` from project `p200001`:

```shell
melctl projects del-user p200001 -m u100001 u100002
```

### `del-coord` - Remove coordinators from a project

```shell
melctl projects del-coord PROJECT -m USER [USER ...]
```

Example to remove coordinators `u100001` and `u100002` from project `p200001`:

```shell
melctl projects del-coord p200001 -m u100001 u100002
```

### `add-sharedfs` - Add shared file system tier to a project

```shell
melctl projects add-sharedfs PROJECT --tier TIER --owner USER
```

Example to add a tier 2 shared filesystem directory owned by user `u100001`
to project `p200001`:

```shell
melctl projects add-sharedfs p200001 --tier 2 --owner u100001
```

### `set-quotas` - Set a project quotas

```shell
melctl projects set-quotas PROJECT \
    [--tier TIER --kbytes KBYTES --inodes INODES] \
    [--cpu MINUTES] \
    [--gpu MINUTES] \
    [--mem MINUTES] \
    [--fpga MINUTES] \
```

Example to set both tier 2 and GPU quotas:

```shell
melctl projects set-quotas p200001 \
    --tier 2 --kbytes 1048576000 --inodes 1000000 \
    --gpu $((3000*60))
```

Example to set tier 2 quotas:

```shell
melctl projects set-quotas p200001 \
    --tier 2 --kbytes 1048576000 --inodes 1000000
```

Example to set CPU and FPGA quotas:

```shell
melctl projects set-quotas p200001 \
    --cpu $((1000*60))
    --fpga $((3000*60))
```

---
