# How to make a release

1. create a new release branch `git checkout -b release/X.Y.Z`
1. bump the package version `uv run bump-my-version bump --new-version X.Y.Z`
1. commit the changes `git commit -m "bump version to X.Y.Z"`
1. push the changes `git push origin release/X.Y.Z`
1. create a pull request to merge the changes into the main branch `gh pr create --base main`
1. merge the pull request `gh pr merge `
1. create a new release on GitHub `gh release create X.Y.Z`


# Automatic version bump

✅ How It Works
1. When you commit code, pre-commit runs all hooks in order
1. After all other hooks pass, the version bumping hook runs
1. It reads the current version (e.g., 0.1.1)
1. Increments the build number (e.g., 0.1.2)
1. Updates all version references in the project
1. Stages the changes automatically
1. The commit proceeds with the updated version

The automatic version bumping is now handled by `bump-my-version` which:
1. Uses the configuration in `pyproject.toml`
1. Increments the build number by 1
1. Updates all version references in:
    1. VERSION file
    1. pyproject.toml
    1. src/app/__init__.py
    1. tests/app/__init__.py
1. Automatically stages the version changes
