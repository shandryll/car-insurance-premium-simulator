from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from src.dto.insurance_dto import InsuranceInputDTO, InsuranceOutputDTO

from .calculate import calculate_insurance

router = APIRouter()


@router.post(
    "/calculate",
    tags=["Calculate Car Insurance Premium"],
    summary="Calculate car insurance premium",
    description=(
        """
        This endpoint calculates car insurance details based on the input data provided,
        such as car details, deductible percentage, and broker fees. It returns the applied rate,
        policy limit, deductible value, and calculated premium.
        """
    ),
    responses={
        200: {
            "description": "Successfully calculated the car insurance premium.",
            "content": {
                "application/json": {
                    "example": {
                        "car": {
                            "make": "Toyota",
                            "model": "Corolla",
                            "year": 2020,
                            "value": 20000.0,
                        },
                        "applied_rate": 0.05,
                        "policy_limit": 18000.0,
                        "calculated_premium": 18500.0,
                        "deductible_value": 2000.0,
                    },
                },
            },
        },
        400: {
            "description": "Bad request. Missing or invalid configuration values.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Validation failed: <errors>",
                    },
                },
            },
        },
        500: {
            "description": "Internal server error. Unexpected error occurred.",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "An unexpected error occurred: <error>",
                    },
                },
            },
        },
    },
)
async def execute(data: InsuranceInputDTO) -> InsuranceOutputDTO:
    try:
        return calculate_insurance(data)
    except ValidationError as ve:
        raise HTTPException(
            status_code=400,
            detail=f"Validation failed: {ve.errors()}",
        ) from ve
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}",
        ) from e
