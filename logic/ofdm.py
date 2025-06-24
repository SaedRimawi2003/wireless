def calculate_ofdm_throughput(modulation_order, subcarriers_per_rb, symbols_per_slot, slots_per_second, num_rbs,
                              cp_overhead_percent, bandwidth_mhz):
    re_rate = modulation_order
    symbol_rate = subcarriers_per_rb * modulation_order
    rb_rate = re_rate * subcarriers_per_rb * symbols_per_slot
    total_rate_bps = rb_rate * num_rbs * slots_per_second
    cp_factor = 1 - (cp_overhead_percent / 100)
    net_rate_bps = total_rate_bps * cp_factor
    spectral_efficiency = net_rate_bps / (bandwidth_mhz * 1e6)

    return {
        "re_rate_bits": re_rate,
        "symbol_rate_bits": symbol_rate,
        "rb_rate_bits": rb_rate,
        "total_rate_bps": round(net_rate_bps),
        "spectral_efficiency_bps_per_hz": round(spectral_efficiency, 4)
    }
