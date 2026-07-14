# Python Package + CLI Template

Template repository for building and publishing Python packages that also expose a
CLI utility.

## Included tooling

- [uv](https://docs.astral.sh/uv/) for dependency management and fast virtualenvs
- [hatchling](https://hatch.pypa.io/latest/) for package builds
- [bump-my-version](https://github.com/callowayproject/bump-my-version) for manual semver bumps
- [fire](https://github.com/google/python-fire) for CLI command generation
- [ruff](https://github.com/astral-sh/ruff) for linting and formatting
- [mypy](https://mypy-lang.org/) for type checking
- [pytest](https://docs.pytest.org/) and pytest-cov for tests and coverage
- [GitHub Actions](https://github.com/features/actions) for CI/CD
- [MkDocs](https://www.mkdocs.org/) for project documentation
- [Docker](https://www.docker.com/) for container builds and runtime packaging

## Why this template is CI/CD-friendly

- CI runs quality checks on Python 3.14 and compatibility tests on 3.11-3.13.
- CI verifies package build artifacts (`sdist` and wheel) and smoke-tests the CLI.
- Release automation is tag-based (`vX.Y.Z`) which is the common Python packaging workflow.
- Docker workflow validates tests in container builds and publishes images on non-PR events.

## Setup

1. Create a new repository from this template.
2. Clone it locally: `git clone <repo-url> && cd <repo-name>`.
3. Install uv (see <https://docs.astral.sh/uv/getting-started/installation/>).
4. Rename the template package:
   - `project.name` in `pyproject.toml`
   - package folder `src/app/` and `tests/app/`
   - CLI script name under `[project.scripts]`
5. Update `.python-version` and `requires-python` in `pyproject.toml`.
6. Install dependencies: `uv sync --group dev`. For Jupyter support, also run `uv sync --group jupyter` (see [Jupyter how-to](docs/how-to/jupyter.md)).
7. Install hooks: `uv run pre-commit install`.
8. Update `.github/CODEOWNERS`.

## Common commands

```bash
# Lint + format check
uv run ruff check .
uv run ruff format --check .

# Type checking
uv run mypy src

# Tests
uv run pytest

# Run CLI
uv run app hello
uv run app version
uv run app --version  # compatibility alias

# Jupyter (install first: uv sync --group jupyter)
uv run jupyter lab
# Use notebooks in notebooks/; see docs/how-to/jupyter.md to add the uv venv as kernel.

# Build package artifacts
uv build
```

## Release process (tag-based)

1. Bump version: `uv run bump-my-version bump patch` (or minor/major).
2. Commit and push the version change.
3. Create and push a tag: `git tag vX.Y.Z && git push origin vX.Y.Z`.
4. GitHub Actions builds artifacts and creates a GitHub release.
5. Optional: set repository variable `PUBLISH_TO_PYPI=true` to publish from the release workflow.

## Documentation

- Project docs index: [docs/index.md](docs/index.md)
- How-to guides: [docs/how-to/index.md](docs/how-to/index.md)
