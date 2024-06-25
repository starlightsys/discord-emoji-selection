# MS Forms survey result CSV reparser

## Setup

### With direnv

First time setup only

```sh
direnv allow
```

### Without direnv

```sh
nix develop
```

## Running it

### One-time

```sh
poetry run python -m csv-reparse
```

### Automatically on file modification

```sh
./watch.nix.sh
```
