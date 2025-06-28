from fastapi import APIRouter

router = APIRouter()

@router.get("/link-budget")
def get_link_budget(
    pr_sensitivity_dbm: float,
    gt_dbi: float,
    gr_dbi: float,
    ar_gain: float,
    lp_db: float,
    lf_db: float,
    l0_db: float,
    fade_margin_db: float
):
    from logic.link_budget import calculate_link_budget_full  # استدعاء الدالة

    result = calculate_link_budget_full(
        pr_sensitivity_dbm=pr_sensitivity_dbm,
        gt_dbi=gt_dbi,
        gr_dbi=gr_dbi,
        ar_gain=ar_gain,
        lp_db=lp_db,
        lf_db=lf_db,
        l0_db=l0_db,
        fade_margin_db=fade_margin_db
    )
    return {
        "Transmit Power (dBm)": result["Transmit Power (dBm)"],
        "Received Power (dBm)": result["Received Power (dBm)"]
    }
