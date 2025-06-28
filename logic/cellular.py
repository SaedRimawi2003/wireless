import math

def erlang_b(channels, traffic):
    """
    حساب احتمال الحجب باستخدام معادلة Erlang B.
    channels: عدد القنوات
    traffic: الحمل (Erlang)
    """
    if channels == 0:
        return 1.0
    inv_b = 1.0
    for k in range(1, channels + 1):
        inv_b = 1.0 + (k / traffic) * inv_b if traffic > 0 else float('inf')
    return 1.0 / inv_b

def calculate_cellular_design(data):
    # استخراج المدخلات
    time_slots_per_carrier = data["time_slots_per_carrier"]
    total_area = data["total_area"]
    max_number_of_users = data["max_number_of_users"]
    number_of_calls_per_day = data["number_of_calls_per_day"]
    call_duration = data["call_duration"]
    gos = data["gos"]
    sir = data["sir"]
    p0 = data["p0"]
    receiver_sensitivity = data["receiver_sensitivity"]
    d0 = data["d0"]
    path_loss_exponent = data["path_loss_exponent"]
    co_channel_interferers = data["co_channel_interferers"]

    # dB إلى watt
    sir_watt = 10 ** (sir / 10)
    p0_watt = 10 ** (p0 / 10)

    if receiver_sensitivity <= 0 or path_loss_exponent <= 0:
        raise ValueError("Receiver sensitivity and path loss exponent must be greater than zero.")

    # a) Max distance
    max_distance = d0 * (p0_watt / receiver_sensitivity) ** (1 / path_loss_exponent)
    max_distance = max(max_distance, 1.0)  # ضمان أنه على الأقل 1 متر

    # b) Max cell size
    max_cell_size = (3 * math.sqrt(3) / 2) * (max_distance ** 2)
    max_cell_size = max(max_cell_size, 1.0)  # ضمان أنه على الأقل 1 م²

    # c) Number of cells
    number_of_cells = math.ceil(total_area / max_cell_size)

    # d) Traffic load
    call_duration_sec = call_duration * 60
    traffic_load_per_user = (number_of_calls_per_day * call_duration_sec) / (24 * 3600)
    traffic_load_system = traffic_load_per_user * max_number_of_users
    traffic_load_cell = traffic_load_system / number_of_cells if number_of_cells > 0 else 0

    # e) Cluster cells
    cluster_cells_real = ((sir_watt * co_channel_interferers) ** (2 / path_loss_exponent)) / 3
    valid_cluster_sizes = sorted({i**2 + i*j + j**2 for i in range(11) for j in range(11) if i**2 + i*j + j**2 > 0})
    cluster_cells = min((n for n in valid_cluster_sizes if n >= cluster_cells_real), default=max(valid_cluster_sizes))

    # f) Channels needed
    channels_needed = 1
    if traffic_load_cell > 0:
        while erlang_b(channels_needed, traffic_load_cell) > gos:
            channels_needed += 1
            if channels_needed > 5000:  # حماية من loop لا نهائي
                break

    # g) Min carriers
    min_carriers = math.ceil(channels_needed * cluster_cells / time_slots_per_carrier) if time_slots_per_carrier > 0 else 0

    return {
        "success": True,
        "results": {
            "max_distance": f"{max_distance:.2f} meters",
            "max_cell_size": f"{max_cell_size:.2f} m²",
            "number_of_cells": f"{number_of_cells} cells",
            "traffic_load_system": f"{traffic_load_system:.2f} Erlang",
            "traffic_load_cell": f"{traffic_load_cell:.2f} Erlang",
            "cluster_cells": f"{cluster_cells} cells",
            "channels_needed": f"{channels_needed} channels",
            "min_carriers": f"{min_carriers} carriers"
        }
    }
