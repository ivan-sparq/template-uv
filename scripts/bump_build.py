#!/usr/bin/env python3
"""Script to increment the build number using bump-my-version logic."""

import re
import subprocess
import sys
from pathlib import Path


def main() -> None:
    """Increment the build number using bump-my-version logic."""
    try:
        # Read current version from VERSION file
        version_file = Path("VERSION")
        current_version = version_file.read_text().strip()

        # Use the same regex as bump-my-version config in pyproject.toml
        regex = re.compile(
            r"""
          (?P<major>\d+)
          \.
          (?P<minor>\d+)
          \.
          ((?P<release>[a-z]+)?
          (?P<build>\d+))
          """,
            re.VERBOSE,
        )

        match = regex.match(current_version)
        if not match:
            print(f"Version {current_version} does not match expected format")
            sys.exit(1)

        groups = match.groupdict()
        major = int(groups["major"])
        minor = int(groups["minor"])
        release = groups["release"] if groups["release"] else ""
        build = int(groups["build"])

        # Increment build number
        new_build = build + 1
        new_version = (
            f"{major}.{minor}.{release}{new_build}"
            if release
            else f"{major}.{minor}.{new_build}"
        )

        print(f"Bumping version from {current_version} to {new_version}")

        # Update VERSION file
        version_file.write_text(f"{new_version}\n")

        # Update pyproject.toml
        pyproject = Path("pyproject.toml")
        pyproject_text = pyproject.read_text()
        pyproject_text = pyproject_text.replace(
            f'version = "{current_version}"', f'version = "{new_version}"'
        )
        # Update bump-my-version config
        pyproject_text = pyproject_text.replace(
            f'current_version = "{current_version}"',
            f'current_version = "{new_version}"',
        )
        pyproject.write_text(pyproject_text)

        # Update all __init__.py files
        for init_file in Path("src").rglob("__init__.py"):
            init_text = init_file.read_text()
            init_text = init_text.replace(
                f'__version__ = "{current_version}"', f'__version__ = "{new_version}"'
            )
            init_file.write_text(init_text)

        for init_file in Path("tests").rglob("__init__.py"):
            init_text = init_file.read_text()
            init_text = init_text.replace(
                f'__version__ = "{current_version}"', f'__version__ = "{new_version}"'
            )
            init_file.write_text(init_text)

        # Add the modified files to git
        subprocess.run(["git", "add", "."], check=True)

        print(f"Version bumped successfully to {new_version}")

    except Exception as e:
        print(f"Error bumping version: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
