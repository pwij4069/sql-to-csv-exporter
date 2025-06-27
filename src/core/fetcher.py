# core/fetcher.py
import logging
from query_builders.header_builder import fetch_data as fetch_header_data
from query_builders.detail_builder import fetch_data as fetch_detail_data

logger = logging.getLogger(__name__)

def fetch_data_by_table(cursor, table, query_tuple):
    if table == "header":
        return fetch_header_data(cursor, query_tuple)
    elif table == "detail":
        return fetch_detail_data(cursor, query_tuple)
    else:
        logger.error(f"No fetcher implemented for table: {table}")
        raise ValueError(f"No fetcher implemented for table: {table}")
