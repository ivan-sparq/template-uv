import logging
import sys
from typing import TextIO


def setup_logging(
    level: int = logging.INFO,
    stream: TextIO | None = None,
    log_format: str | None = None,
    suppress_third_party_libraries: list[str] | None = None,
) -> None:
    """Configure root logging and suppress noisy third-party loggers.

    Args:
        level: The logging level to use.
        stream: The text stream used by logging. Defaults to stderr.
        log_format: Optional custom log format string.
        suppress_third_party_libraries: Additional library logger names to silence.
    """
    resolved_stream = stream if stream is not None else sys.stderr

    resolved_format = log_format
    if resolved_format is None:
        resolved_format = (
            "%(asctime)s.%(msecs)03d %(levelname)s %(name)s "
            "%(filename)s:%(lineno)d] %(message)s"
        )

    logging.basicConfig(
        level=level,
        format=resolved_format,
        datefmt="%m%d %H:%M:%S",
        stream=resolved_stream,
        force=True,
    )

    resolved_libraries = suppress_third_party_libraries or []
    for library in [
        "urllib3",
        "requests",
        "py4j",
        "httpx",
        "matplotlib",
        *resolved_libraries,
    ]:
        logging.getLogger(library).setLevel(logging.ERROR)
