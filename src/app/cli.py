"""Command-line interface for the application template."""

from __future__ import annotations

import logging
import sys

import fire

from app import __version__
from app._logging import setup_logging

_LOG_LEVELS: dict[str, int] = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}


class AppCli:
    """Fire-powered command collection for the template CLI."""

    def hello(self, name: str = "world", log_level: str = "info") -> str:
        """Return a greeting message.

        Args:
            name: Name used in the greeting output.
            log_level: Runtime log level.

        Returns:
            Greeting text.

        Raises:
            ValueError: If the provided log level is unsupported.
        """
        normalized_log_level = log_level.lower()
        configured_level = _LOG_LEVELS.get(normalized_log_level)
        if configured_level is None:
            supported_levels = ", ".join(sorted(_LOG_LEVELS))
            raise ValueError(
                f"Unsupported log level '{log_level}'. "
                f"Supported values: {supported_levels}."
            )

        setup_logging(level=configured_level)
        logger = logging.getLogger(__name__)
        logger.debug("Executing hello command for %s", name)
        return f"Hello, {name}!"

    def version(self) -> str:
        """Return the package version string.

        Returns:
            Package version.
        """
        return __version__

def run(argv: list[str] | None = None) -> int:
    """Execute the CLI command and return an exit code.

    Args:
        argv: Optional command-line arguments. If omitted, uses sys.argv.

    Returns:
        Process exit code.
    """
    resolved_argv = list(argv) if argv is not None else sys.argv[1:]

    if resolved_argv in (["--version"], ["-V"]):
        print(__version__)
        return 0

    fire.Fire(component=AppCli(), command=resolved_argv, name="app")
    return 0


def main() -> None:
    """Run the CLI and exit with the returned code."""
    raise SystemExit(run())
