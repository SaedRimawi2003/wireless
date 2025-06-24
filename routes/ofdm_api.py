from fastapi import APIRouter
from logic.ofdm import calculate_ofdm_throughput

router = APIRouter()

@router.get("/ofdm-throughput")
def get_ofdm(
    modulation_order: int,
    subcarriers_per_rb: int,
    symbols_per_slot: int,
    slots_per_second: int,
    num_rbs: int,
    cp_overhead_percent: float,
    bandwidth_mhz: float
):
    result = calculate_ofdm_throughput(
        modulation_order,
        subcarriers_per_rb,
        symbols_per_slot,
        slots_per_second,
        num_rbs,
        cp_overhead_percent,
        bandwidth_mhz
    )
    return result
