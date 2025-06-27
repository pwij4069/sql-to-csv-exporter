# main.py
import argparse
import sys
import shlex
import json
import os
import logging
from core.connect import get_connection
from core.connect import load_table
from core.query_handler import resolve_query
from core.fetcher import fetch_data_by_table
from core.exporter import export_to_csv
from core.logging_config import setup_logging

logger = logging.getLogger(__name__)

def load_args_from_file(filepath):
    args_list = []
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                args_list.extend(shlex.split(line))
    return args_list

setup_logging()
table = load_table()

# If no CLI args given, load from files
if len(sys.argv) == 1:
    combined_args = []
    combined_args.extend(load_args_from_file("data/common_inputs.txt"))
    combined_args.extend(load_args_from_file(f"data/{table}_inputs.txt"))
    sys.argv.extend(combined_args)
# Parse CLI arguments
parser = argparse.ArgumentParser(description="Export data from DB to CSV.")

def parse_param_type(param_type):
    if param_type == "int":
        return int
    if param_type == "str":
        return str
    if param_type == "list":
        return lambda s: s.split(",")
    return str

# Load parameters
def load_params(t):
    with open("config/common_params.json") as f:
        required_params = json.load(f)
    with open(f"config/{t}_params.json") as f:
        other_params = json.load(f)
    return required_params + other_params

# Register parameters
param_defs = load_params(table)

for param in param_defs:
    kwargs = {
        "help": param.get("help", ""),
        "required": param.get("required", False),
        "type": parse_param_type(param.get("type", "str"))
    }
    if "choices" in param:
        kwargs["choices"] = param["choices"]
    parser.add_argument(f"--{param['name']}", **kwargs)

args = parser.parse_args()

# Get database connection
conn = get_connection(args.env)
if conn is None:
    logger.error("Failed to connect. Exiting.")
    exit(1)

cur = conn.cursor()

# Resolve the correct SQL query
query, error = resolve_query(
    limit=args.limit,
    select_key=args.select,
    columns=args.columns,
    schema=args.schema,
    table=args.table,
    **{k: v for k, v in vars(args).items() if k not in ['env', 'limit', 'select', 'columns', 'schema', 'table']}
)

if error:
    logger.error(error)
    cur.close()
    conn.close()
    exit(1)

# Execute query
results = fetch_data_by_table(cur, args.table, query)
logger.info(f"Fetched {len(results)} rows.")

# Preview results
logger.info("Preview of the first 5 rows:")
for row in results[:5]:
    print(row)
logger.info("...")

# Export to CSV
export_to_csv(cur, results)

logger.info("Closing database connection and cursor.")
cur.close()
conn.close()
