# S8S

Interacts with LuxProvide's Kubernetes-on-HPC (aka. _Slurmenetes_ aka. _S8S_) service.


## Usage

```shell
melctl s8s {list-regions,list-pools,get-pool,scale} [arguments]
```


### `list-regions` - List S8S regions

```shell
melctl s8s list-regions [arguments]
```

Example return as table:

```
name            kind       description
--------------  ---------  ------------------------------
meluxina-test   slurm      LuxProvide HPC (test cluster)
lxp-test.cloud  openstack  LuxProvide Cloud (test tenant)
```

Example return as YAML:

```yaml
- description: LuxProvide HPC (test cluster)
  kind: slurm
  name: meluxina-test
- description: LuxProvide Cloud (test tenant)
  kind: openstack
  name: lxp-test.cloud
```


### `list-pools` - List S8S pools in a given region

```shell
melctl s8s list-pools {region} [arguments]
```

Example return as table:

```
TODO
```

Example return as YAML:

```yaml
- TO: DO
```


### `get-pool` - Get a specific pool information

```shell
melctl s8s get-pool {region} {pool} [arguments]
```

Example return as table:

```
TODO
```

Example return as YAML:

```yaml
- TO: DO
```


### `scale` - Manually scale a K8S/S8S cluster

```shell
melctl s8s scale {region} {pool} {master_node_url}
    --token {master_node_token}
    [ --cpu:{cpu_nodes_count }:{cpu_nodes_seconds }]
    [ --gpu:{gpu_nodes_count }:{gpu_nodes_seconds }]
    [ --mem:{mem_nodes_count }:{mem_nodes_seconds }]
    [--fpga:{fpga_nodes_count}:{fpga_nodes_seconds}]
    [arguments]
```

Example return as table:

```
TODO
```

Example return as YAML:

```yaml
- TO: DO
```

---
