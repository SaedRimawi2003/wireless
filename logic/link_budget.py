import math

def calculate_link_budget(tx_power, tx_gain, rx_gain, frequency_mhz, distance_km):
    path_loss = 20 * math.log10(frequency_mhz) + 20 * math.log10(distance_km) + 32.45
    received_power = tx_power + tx_gain + rx_gain - path_loss
    return {
        "path_loss_db": round(path_loss, 2),
        "received_power_dbm": round(received_power, 2)
    }
