from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from src.config import get_settings

settings = get_settings()

router = APIRouter()


@router.get(
    "/config/",
    tags=["Configuration Check"],
    summary="Check the application's configuration",
    description=(
        """
        This endpoint provides the configuration details of the car insurance.
        It includes information about the car, deductible percentage, broker fee,
        and the registration location.
        """
    ),
    responses={
        200: {
            "description": "Successful response containing the configuration details.",
            "content": {
                "application/json": {
                    "example": {
                        "car": {
                            "make": "Toyota",
                            "model": "Corolla",
                            "year": 2020,
                            "value": 20000,
                        },
                        "deductible_percentage": 0.1,
                        "broker_fee": 500,
                        "registration_location": {
                            "street": "Main Street",
                            "number": "123",
                            "neighborhood": "Downtown",
                            "city": "New York",
                            "state": "NY",
                            "country": "USA",
                            "postal_code": "10001",
                        },
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
async def read_config() -> dict:
    try:
        return {
            "car": {
                "make": settings.car_make,
                "model": settings.car_model,
                "year": settings.car_year,
                "value": settings.car_value,
            },
            "deductible_percentage": settings.deductible_percentage,
            "broker_fee": settings.broker_fee,
            "registration_location": {
                "street": settings.address_street,
                "number": settings.address_number,
                "neighborhood": settings.address_neighborhood,
                "city": settings.address_city,
                "state": settings.address_state,
                "country": settings.address_country,
                "postal_code": settings.address_postal_code,
            },
        }
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
