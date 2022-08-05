# MelCtl - Client - Projects

Manage MeluXina projects.

## Usage

```shell
melctl config {list,get,report} [common args]
```

### List all projects

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

### Get a project information

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

### Get projects resource usage

```shell
melctl projects report [name] \
    [-r,--rangetime lastmonth] \
    [-s,--starttime TIME_START>] \
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

### Create a project

TODO

### Setup a project

TODO

---
