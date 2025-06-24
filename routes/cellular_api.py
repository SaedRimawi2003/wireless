from fastapi import APIRouter
from pydantic import BaseModel
from logic.cellular import calculate_cellular_design

router = APIRouter()

class CellularInput(BaseModel):
    total_area_km2: float
    cell_radius_km: float
    cluster_size: int
    reuse_factor: int = 1  # افتراضيًا 1 إذا لم يُحدّد

@router.post("/cellular-design")
def cellular_design(input: CellularInput):
    return calculate_cellular_design(input)
