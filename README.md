# Python Template

Features:

- [uv](https://docs.astral.sh/uv/) for dependency management
- [hatch](https://hatch.pypa.io/latest/) for building and publishing
- [tbump](https://github.com/your-tools/tbump) for version bumping
- [ruff](https://github.com/astral-sh/ruff) for linting
- [pre-commit](https://pre-commit.com/) for pre-commit hooks
- [GitHub Actions](https://github.com/features/actions) for CI/CD
- [mkdocs](https://www.mkdocs.org/) for documentation
- [Docker](https://www.docker.com/) for containerization

# Setup / using this template

1. In GitHub create a new repository and select this template
1. Clone the repository to your local machine `git clone <repo-url> && cd <repo-name>`
1. Make sure you have uv installed `brew install uv`
1. Rename your app in: `pyproject.toml`, `src/app/` `tests/app/`
1. Update the python version in `.python-version` to match your needs
1. Run `uv sync` to install the dependencies
1. Update the .github/CODEOWNERS file with your github username
1. update your package version with `tbump`. See `docs/how-to/release-process.md`
1. Delete this section of the README.md file and replace it with your own content

---

# My Python Project

Python project template with uv

[Documentation](docs/index.md)
# test
