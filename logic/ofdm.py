def calculate_ofdm_throughput(modulation, total_bandwidth_khz, bandwidth_per_rb_khz, subcarrier_spacing_khz,
                              num_ofdm_symbols, time_for_symbol_ms, num_parallel_rbs):
    # Lookup table for modulation parameters
    modulation_table = {
        "QPSK": {"bits_per_symbol": 2, "coding_rate": 0.5},
        "16QAM": {"bits_per_symbol": 4, "coding_rate": 0.75},
        "64QAM": {"bits_per_symbol": 6, "coding_rate": 0.83},
        "256QAM": {"bits_per_symbol": 8, "coding_rate": 0.93}
    }

    params = modulation_table.get(modulation)
    if not params:
        return {"error": "Unsupported modulation type"}

    bits_per_symbol = params["bits_per_symbol"]
    coding_rate = params["coding_rate"]

    # Number of RBs
    number_of_rbs = total_bandwidth_khz / bandwidth_per_rb_khz

    # Number of subcarriers
    num_subcarriers = bandwidth_per_rb_khz / subcarrier_spacing_khz

    # Number of REs per RB
    num_res = num_ofdm_symbols * num_subcarriers

    # Number of REs for system
    num_res_system = num_res * number_of_rbs

    # Rate for REs
    rate_res = num_res * (bits_per_symbol / (time_for_symbol_ms * 1e-3))  # bps

    # Rate for RBs
    rate_rbs = number_of_rbs * rate_res

    # OFDM rate
    ofdm_rate = rate_res * num_subcarriers

    # Maximum capacity
    maximum_capacity = rate_rbs * num_parallel_rbs * coding_rate  # Include coding rate

    # Spectral efficiency
    spectral_efficiency = maximum_capacity / (total_bandwidth_khz * 1e3)  # bps/Hz

    return {
        "bits_per_symbol": bits_per_symbol,
        "coding_rate": coding_rate,
        "number_of_rbs": number_of_rbs,
        "num_subcarriers_per_rb": num_subcarriers,
        "num_res_per_rb": num_res,
        "num_res_system": num_res_system,
        "rate_res_bps": round(rate_res),
        "rate_rbs_bps": round(rate_rbs),
        "ofdm_rate_bps": round(ofdm_rate),
        "maximum_capacity_bps": round(maximum_capacity),
        "spectral_efficiency_bps_per_hz": round(spectral_efficiency, 4)
    }
