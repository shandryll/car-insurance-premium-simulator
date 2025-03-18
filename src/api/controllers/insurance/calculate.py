from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from src.dto.insurance_dto import InsuranceInputDTO, InsuranceOutputDTO
from src.use_cases.factories.make_calculate_dynamic_rate import make_calculate_dynamic_rate_use_case
from src.use_cases.factories.make_calculate_policy_limit import make_calculate_policy_limit_use_case
from src.use_cases.factories.make_calculate_premium import make_calculate_premium_use_case

router = APIRouter()


@router.post("/calculate", tags=["Calculate Insurance"], summary="Route to calculates car insurance")
def calculate(data: InsuranceInputDTO) -> JSONResponse:
    """."""
    try:
        calculate_dynamic_rate_use_case = make_calculate_dynamic_rate_use_case()
        calculate_premium_use_case = make_calculate_premium_use_case()
        calculate_policy_limit_use_case = make_calculate_policy_limit_use_case()

        applied_rate = calculate_dynamic_rate_use_case.execute(data)
        calculated_premium = calculate_premium_use_case.execute(data, applied_rate)
        policy_calculations = calculate_policy_limit_use_case.execute(data)
        policy_limit = policy_calculations["policy_limit"]
        deductible_value = policy_calculations["deductible_value"]

        response = InsuranceOutputDTO(
            car=data.car,
            applied_rate=applied_rate,
            policy_limit=policy_limit,
            calculated_premium=calculated_premium,
            deductible_value=deductible_value,
        )

        response = response.model_dump_json()

        return JSONResponse(
            content={"car_insurance": response},
            status_code=200,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
