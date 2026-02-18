# How to write/read documentation

1. Add a new markdown file to the docs folder.
2. Add a link to the file in its parent folder's `index.md` file.
3. Update `mkdocs.yml` navigation if you want it visible in the sidebar.

# How-to build the docs to HTML

1. Run `uv run mkdocs build` from the repository root.
2. The HTML files will be in the `site` folder.

3. Run `uv run mkdocs serve` for local preview.
