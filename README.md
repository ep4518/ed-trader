# ed_trader

![PyPI version](https://img.shields.io/pypi/v/ed-trader.svg)

Event Driven Trading System

* GitHub: https://github.com/ep4518/ed-trader/
* PyPI package: https://pypi.org/project/ed-trader/
* Created by: **[Edward Peterson](https://edwardpeterson.com)** | GitHub https://github.com/ep4518 | PyPI https://pypi.org/user/ep4518/
* Free software: MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://ep4518.github.io/ed_trader/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/ed-trader.git
cd ed-trader

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `ed_trader`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

ed_trader was created in 2026 by Edward Peterson.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
