# How to make a release

This template follows a **tag-based release model**.

## 1) Update version

Pick one:

- Patch release: `uv run bump-my-version bump patch`
- Minor release: `uv run bump-my-version bump minor`
- Major release: `uv run bump-my-version bump major`

This updates version references configured in `pyproject.toml`.

## 2) Commit and merge

1. Commit the version bump.
2. Open a PR and merge to your release branch (usually `main`).

## 3) Create and push a tag

```bash
git tag vX.Y.Z
git push origin vX.Y.Z
```

The release workflow will:

1. Build wheel and source distributions.
2. Create a GitHub Release and attach artifacts.
3. Optionally publish to PyPI if `PUBLISH_TO_PYPI=true` is configured.

## Why this model

- Explicit semantic versioning decisions.
- Reproducible release history tied to immutable tags.
- Compatible with standard Python packaging automation.
