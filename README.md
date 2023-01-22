# Cookiecutter Template for Python Project

This is a basic template for minimal Python packages, with the option to add REST API and other tools I commonly use.

## Features

* [pip](https://github.com/pypa/pip) for package management
* [pre-commit](https://pre-commit.com/) hooks:
  * Linting with [flake8](https://flake8.pycqa.org/en/latest/) (+ plugins)
  * Remove unused imports and variables with [autoflake](https://github.com/myint/autoflake)
  * Sorting imports with [isort](https://github.com/timothycrosley/isort)
  * Code formatting with [black](https://black.readthedocs.io/en/stable/)
  * Static type checking with [mypy](https://mypy.readthedocs.io/)
* [pytest](https://docs.pytest.org/en/latest/) + [pytest-cov](https://pytest-cov.readthedocs.io/) + [pytest-mock](https://github.com/pytest-dev/pytest-mock)

## Setup

Install [cookiecutter](https://github.com/cookiecutter/cookiecutter)

```
cookiecutter <url>
```