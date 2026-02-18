# How to use Jupyter with this project

This guide covers installing Jupyter dependencies and using the project's uv virtualenv as the Jupyter kernel.

## Installing Jupyter dependencies

Dependencies for Jupyter (JupyterLab/Notebook and IPython kernel) are in the optional dependency group `jupyter`. Install them with:

```bash
uv sync --group jupyter
```

To install both dev and Jupyter tools:

```bash
uv sync --group dev --group jupyter
```

Or install all groups:

```bash
uv sync --all-groups
```

## Adding the uv virtualenv as a Jupyter kernel

So that Jupyter uses this project's environment (and can import the app package), register the uv-managed virtualenv as a Jupyter kernel.

1. Activate the project environment and ensure the jupyter group is installed:

   ```bash
   uv sync --group jupyter
   ```

2. Register the current environment as a kernel (run from the project root):

   ```bash
   uv run python -m ipykernel install --user --name=template-uv --display-name="Python (template-uv)"
   ```

   - `--name=template-uv` is the kernel ID (use a name that matches your project).
   - `--display-name="Python (template-uv)"` is the label shown in the Jupyter kernel list.

3. Start Jupyter:

   ```bash
   uv run jupyter lab
   # or
   uv run jupyter notebook
   ```

4. In Jupyter, create or open a notebook and choose **"Python (template-uv)"** (or your display name) as the kernel.

After that, `import app` and the rest of the project package will be available in the notebook.

## Example notebook

The [notebooks/example.ipynb](../../notebooks/example.ipynb) notebook shows how to load the app and call its API from a Jupyter cell.
