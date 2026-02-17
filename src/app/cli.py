"""Command-line interface for the application template."""

from __future__ import annotations

import argparse
import logging

from app import __version__
from app._logging import setup_logging

_LOG_LEVELS: dict[str, int] = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI argument parser.

    Returns:
        Configured argument parser for the CLI.
    """
    parser = argparse.ArgumentParser(
        prog="app",
        description="Template CLI for Python packages.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--log-level",
        choices=sorted(_LOG_LEVELS.keys()),
        default="info",
        help="Log level for runtime diagnostics.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)
    hello_parser = subparsers.add_parser("hello", help="Print a greeting.")
    hello_parser.add_argument(
        "name",
        nargs="?",
        default="world",
        help="Name used in the greeting output.",
    )
    return parser


def run(argv: list[str] | None = None) -> int:
    """Execute the CLI command and return an exit code.

    Args:
        argv: Optional command-line arguments. If omitted, uses sys.argv.

    Returns:
        Process exit code.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    setup_logging(level=_LOG_LEVELS[args.log_level])
    logger = logging.getLogger(__name__)

    match args.command:
        case "hello":
            logger.debug("Executing hello command for %s", args.name)
            print(f"Hello, {args.name}!")
            return 0
        case _:
            parser.error(f"Unsupported command: {args.command}")
            return 2


def main() -> None:
    """Run the CLI and exit with the returned code."""
    raise SystemExit(run())
