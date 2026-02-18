# How to set up your development environment

## Assumptions

- You already cloned this repository.
- You are using VS Code (optional, but recommended).

## Initial setup

1. Install uv (see <https://docs.astral.sh/uv/getting-started/installation/>).
2. Install dependencies: `uv sync --group dev`.
3. Install git hooks: `uv run pre-commit install`.

## Add dependencies

1. Add a runtime dependency: `uv add <dependency>`.
2. Add a dev dependency: `uv add --group dev <dependency>`.
3. Sync after pulling changes from other contributors: `uv sync --group dev`.

## IDE setup

1. Install recommended extensions from `.vscode/extensions.json`.
2. Ensure Ruff is selected as the Python formatter.
