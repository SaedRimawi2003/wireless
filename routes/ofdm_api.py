from fastapi import APIRouter
from logic.ofdm import calculate_ofdm_throughput

router = APIRouter()

@router.get("/ofdm-throughput")
def get_ofdm(
    modulation: str,
    total_bandwidth_khz: float,
    bandwidth_per_rb_khz: float,
    subcarrier_spacing_khz: float,
    num_ofdm_symbols: int,
    time_for_symbol_ms: float,
    num_parallel_rbs: int
):
    result = calculate_ofdm_throughput(
        modulation,
        total_bandwidth_khz,
        bandwidth_per_rb_khz,
        subcarrier_spacing_khz,
        num_ofdm_symbols,
        time_for_symbol_ms,
        num_parallel_rbs
    )
    return {
        "Bits Per Symbol": result["bits_per_symbol"],
        "Coding Rate": result["coding_rate"],
        "Number of RBs": result["number_of_rbs"],
        "Subcarriers per RB": result["num_subcarriers_per_rb"],
        "REs per RB": result["num_res_per_rb"],
        "REs for System": result["num_res_system"],
        "Rate per RE (bps)": result["rate_res_bps"],
        "Rate for RBs (bps)": result["rate_rbs_bps"],
        "OFDM Rate (bps)": result["ofdm_rate_bps"],
        "Maximum Capacity (bps)": result["maximum_capacity_bps"],
        "Spectral Efficiency (bps/Hz)": result["spectral_efficiency_bps_per_hz"]
    }
