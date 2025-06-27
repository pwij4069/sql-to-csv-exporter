# query_handler.py
import logging
from query_builders.header_builder import build_dynamic_query as build_header_query
from query_builders.detail_builder import build_dynamic_query as build_detail_query

logger = logging.getLogger(__name__)

def resolve_query(limit, select_key="all", columns=None, schema=None, table=None, **kwargs):
    logger.debug(f"Query parameters: limit={limit}, select_key={select_key}, columns={columns}, schema={schema}")
    try:
        if table == "header":
            logger.debug("Building query using header builder.")
            query, values = build_header_query(limit, select_key, columns, schema=schema, table=table, **kwargs)
        elif table == "detail":
            logger.debug("Building query using detail builder.")
            query, values = build_detail_query(limit, select_key, columns, schema=schema, table=table, **kwargs)
        else:
            logger.error(f"Unsupported table type: {table}")
            raise ValueError(f"Unsupported table type: {table}")
    except ValueError as e:
        logger.exception("Error occurred while building query")
        return None, str(e)
    return (query, values), None

