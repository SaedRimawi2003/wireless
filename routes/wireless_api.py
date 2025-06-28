from fastapi import APIRouter
from pydantic import BaseModel
from logic.wireless import calculate_wireless_blocks

router = APIRouter()

class WirelessInput(BaseModel):
    bandwidth_hz: float
    cutoff_frequency_hz: float
    quantization_bits: int
    source_encoding_ratio: float
    channel_coding_rate: float
    overhead_percentage: float

@router.post("/wireless-system")
def wireless_system(data: WirelessInput):
    result = calculate_wireless_blocks(data)
    return {
        "Effective Frequency (Hz)": result["effective_frequency_hz"],
        "Sampler Output Rate (Hz)": result["sampler_output_rate"],
        "Quantizer Output Rate (bps)": result["quantizer_output_rate"],
        "Source Encoder Output Rate (bps)": result["source_encoder_output_rate"],
        "Channel Encoder Output Rate (bps)": result["channel_encoder_output_rate"],
        "Interleaver Output Rate (bps)": result["interleaver_output_rate"],
        "Overhead Output Rate (bps)": result["overhead_output_rate"],
        "Burst Formatter Output Rate (bps)": result["burst_formatter_output_rate"]
    }
