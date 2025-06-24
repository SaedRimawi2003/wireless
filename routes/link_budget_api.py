from fastapi import APIRouter
from logic.link_budget import calculate_link_budget

router = APIRouter()

@router.get("/link-budget")
def get_link_budget(
    tx_power: float,
    tx_gain: float,
    rx_gain: float,
    frequency_mhz: float,
    distance_km: float
):
    result = calculate_link_budget(tx_power, tx_gain, rx_gain, frequency_mhz, distance_km)
    return result
