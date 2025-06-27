#header_builder
import json
import logging
from query_builders.header_patterns import selects
from query_builders.header_mapper import PARAM_TO_DB_COLUMN

logger = logging.getLogger(__name__)

# Load parameters
def load_params():
    with open("config/common_params.json") as f:
        required_params = json.load(f)
    with open("config/header_params.json") as f:
        other_params = json.load(f)
    return required_params + other_params

def build_dynamic_query(limit=100, select_key="all_fields", columns=None, schema=None, table=None, **kwargs):
    reserved_keys = {"env", "limit", "select", "columns", "schema", "table"}
    limit = limit or 100

    # Select columns
    if columns:
        selected_columns = columns
        logger.debug(f"Using custom columns: {columns}")
    else:
        selected_columns = selects.get(select_key, selects["all_fields"])
        logger.debug(f"Using select pattern '{select_key}'")

    # Map parameters to DB columns
    where_clauses = []
    values = []

    for key, val in kwargs.items():
        if key in reserved_keys or val in [None, ""]:
            continue

        db_col = PARAM_TO_DB_COLUMN.get(key, key)

        # BETWEEN clause
        if key == "date_from" and "date_to" in kwargs:
            where_clauses.append(f"{PARAM_TO_DB_COLUMN.get('date_from', 'trans_dt')} BETWEEN %s AND %s")
            values.append(val)
            values.append(kwargs["date_to"])
        elif key == "delivery_date_from" and "delivery_date_to" in kwargs:
            where_clauses.append(f"{PARAM_TO_DB_COLUMN.get('delivery_date_from', 'dlvr_dt')} BETWEEN %s AND %s")
            values.append(val)
            values.append(kwargs["delivery_date_to"])
        elif isinstance(val, list):
            # IN / OR clause for lists
            placeholders = " OR ".join([f"{db_col} = %s"] * len(val))
            where_clauses.append(f"({placeholders})")
            values.extend(val)
        else:
            where_clauses.append(f"{db_col} = %s")
            values.append(val)

    # Construct final query
    where_sql = "WHERE " + " AND ".join(where_clauses) if where_clauses else ""
    query = f"SELECT {selected_columns} FROM {schema}.{table} {where_sql} LIMIT %s"
    values.append(limit)
    logger.info(f"Built query: {query} with values {values}")
    return query, values


def fetch_data(cursor, query_tuple):
    if isinstance(query_tuple, tuple):
        cursor.execute(*query_tuple)
    else:
        cursor.execute(query_tuple)
    return cursor.fetchall()