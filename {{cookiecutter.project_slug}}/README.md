# {{cookiecutter.project_slug}} v{{cookiecutter.version}}
 > {{cookiecutter.project_short_description}}

## Technology Stack
- ...

## Installation
1. Download the repository
2. Run `docker compose up -d`
3. ...

## Development notes

...

### Run tests

**Unit testing**
Unit testing can be run by running:
- `pytest -k 'not unstable' tests/unit --cov=my_project --cov-fail-under=100` *(run from inside the pre-configured [VS Code Remote Containers env](https://code.visualstudio.com/docs/remote/containers))*

**Integration testing**
Integration testing can be run by running:
- `pytest -k 'not unstable' tests/integration` *(run from inside the pre-configured [VS Code Remote Containers env](https://code.visualstudio.com/docs/remote/containers))*

### Bump package version
On a new release, version can be updated using `bumpver` tool:

`bumpver update { --major | --minor | --patch }`
