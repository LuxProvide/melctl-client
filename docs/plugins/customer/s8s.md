# S8S

Interacts with LuxProvide's Kubernetes-on-HPC (aka. _Slurmenetes_ aka. _S8S_) service.


## Usage

```shell
melctl s8s {set-config,get-config,del-config,list-regions,list-pools,get-pool,status,resources,scale} [arguments]
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

## Tutorial

S8S is used to scale an **existing** compatible Kubernetes cluster on MeluXina HPC.

### Obtaining a compatible K8S cluster

Please contact LuxProvide.

### Obtaining a cluster token

Once a cluster is created, you'll receive a **join token**; This token will be used
to scale your cluster on MeluXina HPC.

### Setting-up a configuration

!!! note "Optional"
    Setting-up a configuration is not mandatory, but recommend as is simplifies other operations.

!!! note "Configuration update"
    A configuration can be updated by re-creating it.  
    Use `melctl s8s get-config --token` to list the existing configuration(s) with the token before
    updating / recreating a configuration.

Prerequisites:

* Region name (should be `meluxina`, or use the value instructed by LuxProvide)
* Pool name (should be your project ID, e.g. `p200XYZ)`)
* Master URL (given by LuxProvide)
* Join token (given by LuxProvide)

Command:

```shell
melctl s8s set-config ${config_name} \
    --region ${region_name} \
    --pool ${pool_name} \
    --master ${master_url} \
    --token ${join_token}
```

Example:

```shell
melctl s8s set-config default \
    --region meluxina \
    --pool p200001 \
    --master "https://s8s.p200001.cloud.lxp.lu:6443" \
    --token "*****"
```

### List available resources

`melctl s8s resources` returns the available resources for a given region.

Procedure with a pre-existing configuration:

```shell
melctl s8s resources ${config_name}
```

Procedure without configuration:

```shell
melctl s8s resources --region ${region_name}
```

### Scale a cluster

`melctl s8s scale` scales a cluster according to the provided _specifications_.

Specifications are defined as follow:

* The **node type** argument: `--cpu`, `--gpu`, `--mem`, `--fpga`
* The two-part value: `{nodes_count}:{time_seconds}`
    * The **nodes count** value: a number > 0
    * The **allocation time** value: a number > 0

Multiple specifications may be provided.

Procedure with a pre-existing configuration:

```shell
melctl s8s scale ${config_name}
    --${node_type} ${nodes_count}:${time_seconds} # ...
```

Procedure without configuration:

```shell
melctl s8s scale \
    --region ${region_name}
    --pool ${pool_name} \
    --master ${master_url} \
    --token ${join_token} \
    --${node_type} ${nodes_count}:${time_seconds} # ...
```

Example with a pre-existing configuration:

```shell
melctl s8s scale default
    --cpu "1:1800" \
    --cpu "2:3600" \
    --gpu "2:3600"
```

Example without configuration:

```shell
melctl s8s scale \
    --region ${region_name}
    --pool ${pool_name} \
    --master ${master_url} \
    --token ${join_token} \
    --cpu "1:1800" \
    --cpu "2:3600" \
    --gpu "2:3600"
```

### Check status with `melctl`

`melctl s8s status` reports the status of an S8S allocation.

Procedure with a pre-existing configuration:

```shell
melctl s8s status ${config_name}
```

Procedure without configuration:

```shell
melctl s8s scale \
    --region ${region_name}
    --pool ${pool_name} \
    --master ${master_url} \
    --token ${join_token} \
    --${node_type} ${nodes_count}:${time_seconds} # ...
```

### Check status with `kubectl`

`kubectl get nodes` lists the cluster's nodes.

### Cleanup

The allocated Kubernetes nodes are stopped automatically by MelCtl. However,
the Kubernetes cluster should be informed manually that the nodes have been removed.

Run `kubectl delete node ${node_name}` to remove a de-allocated node.

---
