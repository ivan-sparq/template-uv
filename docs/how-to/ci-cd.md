# CI/CD workflow

## Overview

This template provides three CI/CD workflows:

1. **Python CI** (`.github/workflows/python-test.yml`)
   - Quality checks on Python 3.13 (ruff, mypy, pytest with coverage).
   - Compatibility tests on Python 3.10-3.12.
   - Package build and CLI smoke test (`uv build`, wheel install, `app --version`).
2. **Docker Build and Publish** (`.github/workflows/docker-build.yml`)
   - Builds a test image and runs tests inside the container.
   - Builds production image and publishes to GHCR on non-PR events.
3. **Release package from tag** (`.github/workflows/release.yml`)
   - Triggered by `vX.Y.Z` tags.
   - Builds distributions and creates a GitHub Release.
   - Optionally publishes to PyPI if `PUBLISH_TO_PYPI=true`.

## Current approach vs Python packaging best practices

| Topic | Previous setup | Updated setup (best practice) |
|---|---|---|
| Python compatibility | Single-version tests | Version matrix for declared supported versions |
| Release trigger | Auto bump on PR merge | Explicit semver tag-driven release |
| Package validation | No wheel/sdist smoke test | Build artifacts and smoke-test CLI install |
| Docker tests | Build test image only | Build and execute tests in container |
| Dependency update automation | Dependabot scanned wrong directory | Dependabot scans project root + GitHub Actions |

## Why tag-based releases are recommended

- Keeps semantic versioning explicit and intentional.
- Avoids noisy "version bump on every merge" commits.
- Maps naturally to PyPI publishing and GitHub Releases.
- Makes rollback and reproducibility easier.

## How to publish to PyPI

1. Configure GitHub trusted publishing for your PyPI project.
2. Set repository variable: `PUBLISH_TO_PYPI=true`.
3. Push a version tag (`vX.Y.Z`) to trigger publish.
