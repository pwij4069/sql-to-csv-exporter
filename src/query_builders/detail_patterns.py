selects = {
    "all_fields": "*",
    "detail_pattern": (
        "opco_nbr AS \"opcoNumber\", "
        "sale_oblig_trans_id AS \"invoiceNumber\", "
        "item_desc AS \"itemDescription\", "
        "item_nbr AS \"itemNumber\", "
        "ln_nbr AS \"lineNumber\", "
        "trans_dt AS \"transDate\", "
        "orig_ship_qty AS \"originalShipQty\", "
        "orig_ord_qty AS \"originalOrderQty\", "
        "orig_prc AS \"originalPrice\", "
        "item_amt AS \"itemAmount\", "
        "ctch_wgt_ind AS \"catchWeightIndicator\", "
        "splt_cd AS \"splitCode\", "
        "curr_qty AS \"currentQty\", "
        "curr_splt_qty AS \"currentSplitQty\", "
        "curr_prc AS \"currentPrice\", "
        "curr_tot_ctch_wgt AS \"currentTotalCatchWeight\", "
        "sub_item_nbr AS \"subItemNumber\", "
        "ord_rsn_cd AS \"orderReasonCode\""
    ),
    "delivery_item_pattern": (
        "opco_nbr AS \"opcoNumber\", "
        "sale_oblig_trans_id AS \"invoiceNumber\", "
        "item_nbr AS \"itemNumber\", "
        "ln_nbr AS \"lineNumber\", "
        "sch_dlvr_dt AS \"scheduledDeliveryDate\", "
        "qty AS \"quantity\", "
        "dlvrd_item_qty AS \"deliveredItemQty\", "
        "rej_item_qty AS \"rejectedItemQty\""
    ),
    "financial_summary_pattern": (
        "past_due_amt AS \"pastDue\", "
        "cash_on_account_amt AS \"cashOnAccount\", "
        "available_credits_amt AS \"availableCredits\", "
        "current_invoices_amt AS \"currentInvoices\", "
        "balance_due_amt AS \"balanceDue\", "
        "total_balance_amt AS \"totalBalance\""
    )
}
