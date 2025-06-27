# connect.py
import os
import json
import psycopg2
import logging
import shlex
import argparse
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/db_properties.ini")

logger = logging.getLogger(__name__)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT", 5432)

def load_db_config(config_key, config_path="config/db_config.json"):
    try:
        with open(config_path, "r") as f:
            configs = json.load(f)
            if config_key in configs:
                logger.info(f"Database config loaded for key: {config_key}")
                return configs[config_key]
            else:
                logger.error(f"Config key '{config_key}' not found.")
                raise ValueError(f"Config key '{config_key}' not found.")
    except Exception as e:
        logger.exception(f"Failed to load DB config: {e}")
        return None

def get_connection(config_key):
    config = load_db_config(config_key)
    if config is None:
        return None

    try:
        conn = psycopg2.connect(
            host=config["host"],
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=config["database"]
        )
        logging.basicConfig(level=logging.INFO)
        logging.info("Connected to database.")
        return conn
    except psycopg2.Error as e:
        logger.exception(f"Error connecting to the database: {e}")
        return None

def load_table():
    config = load_args("data/common_inputs.txt")
    table = config.get("table")
    logger.debug(f"Loaded table name from common_inputs.txt: {table}")
    return table

def load_args(filepath):
    args_dict = {}
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                tokens = shlex.split(line)
                if len(tokens) >= 2 and tokens[0].startswith("--"):
                    key = tokens[0][2:]  # remove leading --
                    value = tokens[1]
                    args_dict[key] = value
    return args_dict
