import logging

from ._logging import setup_logging

__version__ = "0.3.1"

setup_logging()
logging.info(f"Initializing app v{__version__}")
