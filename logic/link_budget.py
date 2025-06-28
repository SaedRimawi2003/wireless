def calculate_link_budget_full(
    pr_sensitivity_dbm,  # Receiver sensitivity (dBm)
    gt_dbi,              # Transmitter antenna gain (dBi)
    gr_dbi,              # Receiver antenna gain (dBi)
    ar_gain,             # Receiver amplifier gain (dB)
    lp_db,               # Path loss (dB)
    lf_db,               # Feedline loss (dB)
    l0_db,               # Other losses (dB)
    fade_margin_db       # Fade margin (dB)
):
    # Calculate Transmitted Power (dBm)
    pt_dbm = (
        pr_sensitivity_dbm
        + lp_db
        + lf_db
        + l0_db
        + fade_margin_db
        - gt_dbi
        - gr_dbi
        - ar_gain
    )

    # Calculate Received Power (dBm)
    pr_dbm = (
        pt_dbm
        + gt_dbi
        + gr_dbi
        + ar_gain
        - lp_db
        - lf_db
        - l0_db
    )

    return {
        "Transmit Power (dBm)": pt_dbm,
        "Received Power (dBm)": pr_dbm
    }
