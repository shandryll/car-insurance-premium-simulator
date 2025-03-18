from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.dto.insurance_dto import InsuranceInputDTO
from src.use_cases.factories.make_calculate_dynamic_rate import make_calculate_dynamic_rate_use_case

router = APIRouter()


@router.post("/calculate", tags=["Calculate Insurance"], summary="Route to calculates car insurance")
def calculate(data: InsuranceInputDTO) -> JSONResponse:
    """."""
    try:
        # insurance_input = data.model_dump_json()

        calculate_dynamic_rate_use_case = make_calculate_dynamic_rate_use_case()
        dynamic_rate = calculate_dynamic_rate_use_case.execute(data)

        return {"status": "ok"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
