from fastapi import APIRouter
from pydantic import BaseModel
from logic.wireless import calculate_wireless_blocks

router = APIRouter()

class WirelessInput(BaseModel):
    sampling_rate_hz: float
    quantization_bits: int
    source_encoding_ratio: float
    channel_coding_rate: float

@router.post("/wireless-system")
def wireless_system(data: WirelessInput):
    return calculate_wireless_blocks(data)
