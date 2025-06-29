from fastapi import APIRouter
from pydantic import BaseModel
from logic.cellular import calculate_cellular_design
router = APIRouter()

class CellularInput(BaseModel):
    time_slots_per_carrier: int
    total_area: float
    max_number_of_users: int
    number_of_calls_per_day: int
    call_duration: float
    gos: float
    sir: float
    p0: float
    receiver_sensitivity: float
    d0: float
    path_loss_exponent: float
    co_channel_interferers: int

@router.post("/cellular-design")
def cellular_design(data: CellularInput):
    result = calculate_cellular_design(data.dict())
    return result
