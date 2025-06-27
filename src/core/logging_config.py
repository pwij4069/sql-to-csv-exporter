# logging_config.py

import logging
import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()  # can use env var

def setup_logging(log_file: str = "logs/project.log"):
    # directory if not exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        level=LOG_LEVEL,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # log to console
        ]
    )
