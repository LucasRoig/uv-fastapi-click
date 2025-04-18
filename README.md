## Prérequis

### uv

Installer uv, par exemple avec brew : `brew install uv` sinon se référer à la [documentation](https://docs.astral.sh/uv/getting-started/installation/)

### just 

Just est utilisé pour encapsuler les commandes uv. 
Pour l'installer avec brew : `brew install just` sinon se référer à la [documentation](https://github.com/casey/just?tab=readme-ov-file#cross-platform)

## Installation des dépendances

```bash
just install
```

## Lancer l'API

```bash
just api-dev
```

## Lancer l'interface CLI

```bash
just cli --help
```

## Ajout d'une dépendance

Pour ajouter une dépendance, il faut spécifier dans quel pqackage elle doit être ajoutée. Ex: `uv add --package prompt openai`