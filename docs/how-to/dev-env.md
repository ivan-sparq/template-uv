# How to setup your development environment

### Assumptions:

- Assuming you have already have cloned this repository locally
- Assumping you are using VSCode to run the code locally

### Initial setup

1. Install uv `brew install uv` ([How to install brew](https://brew.sh/))
1. `uv sync --extra dev` to install the dependencies
1. `uv run pre-commit install` to install the pre-commit hooks

### Adding new Python dependencies

1. `uv add <dependency>` to add a new Python dependency
1. `uv sync --extra dev` to install the new dependency (e.a. you need to manually run this if someone else has added a dependency)

### IDE setup

1. Install the recommended extension from `.vscode/extensions.json`.
   - Go to the extensions tab in VSCode
   - From the filter icon (next to the search bar) select `Recommended`
   - Click on the little cloud icon that says "Install Workspace Recommended Extensions" when you hover over it
