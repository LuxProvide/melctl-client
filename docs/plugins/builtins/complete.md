# Complete

Generate a MelCtl client autocompletion script.

## Usage

```shell
melctl complete {shell}
```

Example to generate and load the autocomplete script:

```shell
source <(melctl complete $(basename ${SHELL}))
```

## `bash` - Autocompletion for Bash

Generate and load the autocompletion script for Bash:

```shell
source <(melctl complete bash)
```

## `zsh` - Autocompletion for ZSH

Generate and load the autocompletion script for ZSH:

```shell
source <(melctl complete zsh)
```

Alternative:

```shell
melctl complete zsh | source /dev/stdin
```

---
