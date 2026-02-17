"""Tests for the template CLI."""

import pytest

from app import __version__
from app.cli import run


def test_run_hello_default(capsys: pytest.CaptureFixture[str]) -> None:
    """Run the default hello command and verify output."""
    exit_code = run(["hello"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "Hello, world!"


def test_run_hello_name(capsys: pytest.CaptureFixture[str]) -> None:
    """Run the hello command with a custom name."""
    exit_code = run(["--log-level", "debug", "hello", "template"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "Hello, template!"


def test_run_version(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify the version flag renders package metadata."""
    with pytest.raises(SystemExit) as exc_info:
        run(["--version"])

    captured = capsys.readouterr()
    assert exc_info.value.code == 0
    assert __version__ in captured.out
