# Cookiecutter Python

This is a cookiecutter template for a python project. This cookiecutter was
heavily inspired by
[cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python)
but removes items requiring external services such. This cookiecutter includes:


- Packaging and dependency management with [Poetry]
- Test automation with [Nox]
- Linting with [pre-commit] and [Flake8]
- Documentation with [Sphinx] and [MyST] using the [furo] theme
- Code formatting with [Black] and [Prettier]
- Import sorting with [isort]
- Testing with [pytest]
- Command-line interface with [typer]
- Static type-checking with [mypy]
- Runtime type-checking with [Typeguard]
- Check documentation examples with [xdoctest]
- Generate API documentation with [autodoc] and [napoleon]
- Generate command-line reference with [sphinx-click]

[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[bandit]: https://github.com/PyCQA/bandit
[black]: https://github.com/psf/black
[flake8]: http://flake8.pycqa.org
[furo]: https://pradyunsg.me/furo/
[isort]: https://pycqa.github.io/isort/
[mypy]: http://mypy-lang.org/
[myst]: https://myst-parser.readthedocs.io/
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[nox]: https://nox.thea.codes/
[poetry]: https://python-poetry.org/
[pre-commit]: https://pre-commit.com/
[prettier]: https://prettier.io/
[pytest]: https://docs.pytest.org/en/latest/
[sphinx]: http://www.sphinx-doc.org/
[sphinx-click]: https://sphinx-click.readthedocs.io/
[typeguard]: https://github.com/agronholm/typeguard
[typer]: https://typer.tiangolo.com/typer-cli/
[xdoctest]: https://github.com/Erotemic/xdoctest

## Usage

```console
cookiecutter cookiecutter-python
```

Then, change to the project directory and initialize a git repository:

```console
git init
git add .
git commit -m "initial commit"
```

Install poetry environment:

```console
poetry install
```

Install the pre-commit hooks:

```console
nox -s pre-commit -- install
```
