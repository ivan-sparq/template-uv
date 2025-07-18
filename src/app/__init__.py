import logging

from ._logging import setup_logging

__version__ = "0.4.23"

setup_logging()
logging.info(f"Initializing app v{__version__}")
