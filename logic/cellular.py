import math

def calculate_cellular_design(data):
    # مساحة الخلية السداسية
    cell_area = (3 * math.sqrt(3) / 2) * (data.cell_radius_km ** 2)

    # عدد الخلايا اللازمة لتغطية المنطقة
    num_cells = math.ceil(data.total_area_km2 / cell_area)

    # المسافة بين مراكز الخلايا المتكررة (التردد)
    reuse_distance = data.cell_radius_km * math.sqrt(3 * data.cluster_size)

    return {
        "cell_area_km2": round(cell_area, 2),
        "num_cells_required": num_cells,
        "cluster_size": data.cluster_size,
        "frequency_reuse_distance_km": round(reuse_distance, 2)
    }
