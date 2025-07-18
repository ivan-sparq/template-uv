import logging
import sys


def setup_logging(
    level: int = logging.INFO,
    stream: logging.StreamHandler | None = None,
    log_format: str | None = None,
    suppress_third_party_libraries: list[str] | None = None,
) -> None:
    """
    Set up logging with Google's default format.

    Args:
        level: The logging level to use (default: INFO)
        stream: The stream to log to (default: sys.stderr)
        log_format: Optional custom log format string
    """
    if stream is None:
        stream = logging.StreamHandler(sys.stderr)

    if log_format is None:
        # Google's default logging format
        log_format = "%(asctime)s.%(msecs)03d %(levelname)s %(name)s %(filename)s:%(lineno)d] %(message)s"

    formatter = logging.Formatter(
        fmt=log_format,
        datefmt="%m%d %H:%M:%S",
    )
    stream.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    root_logger.addHandler(stream)

    # Deal with None values
    suppress_third_party_libraries = suppress_third_party_libraries or []

    # Set up logging for third-party libraries
    # silence third-party libraries
    for library in [
        "urllib3",
        "requests",
        "py4j",
        "httpx",
        "matplotlib",
        *suppress_third_party_libraries,
    ]:
        logging.getLogger(library).setLevel(logging.ERROR)
