from fastapi import APIRouter
from pydantic import BaseModel
from logic.ai_explain import generate_explanation

router = APIRouter()

class ExplainRequest(BaseModel):
    scenario: str
    data: dict

@router.post("/explain")
def explain(request: ExplainRequest):
    explanation = generate_explanation(request.scenario, request.data)
    return {"explanation": explanation}
