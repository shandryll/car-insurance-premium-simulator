from fastapi import APIRouter

from src.dto.insurance_dto import InsuranceInputDTO, InsuranceOutputDTO

from .calculate import calculate_insurance

router = APIRouter()


@router.post("/calculate", tags=["Calculate Insurance"], summary="Route to calculates car insurance")
def execute(data: InsuranceInputDTO) -> InsuranceOutputDTO:
    """."""
    return calculate_insurance(data)
