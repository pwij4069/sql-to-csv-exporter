# core/header_mapper.py

PARAM_TO_DB_COLUMN = {
    "opco_nbr": "opco_nbr",
    "customer_number": "cust_ship_to_nbr",
    "invoice_number": "sale_oblig_trans_id",
    "opco_nbr_list": "opco_nbr",
    "invoice_numbers": "sale_oblig_trans_id",
    "date_from": "trans_dt",
    "date_to": "trans_dt",
    "delivery_date_from": "dlvr_dt",
    "delivery_date_to": "dlvr_dt",
    "seller_id": "seller_id",
    "additional_seller_providers": "original_seller_id",
    "invoice_status": "trans_cd",
    "invoice_source": "oblig_src_cd",
    "clean_status": "posted_to_financials",
    "poNumber": "po_number",
    "sourceNumber": "src_nbr",
    "originalCaseCount": "orig_case_cnt",
    "currentCaseCount": "curr_case_cnt"
    # Add all other mappings...
}
