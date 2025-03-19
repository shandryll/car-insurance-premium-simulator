from fastapi import APIRouter
from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings

router = APIRouter()


class Settings(BaseSettings):
    car_make: str = Field(..., min_length=1, description="The manufacturer of the car. Cannot be empty.")
    car_model: str = Field(..., min_length=1, description="The model of the car. Cannot be empty.")
    car_year: int = Field(..., ge=1886, description="The year of the car. Must be 1886 or later.")
    car_value: float = Field(..., gt=0, description="The value of the car. Must be greater than zero.")
    deductible_percentage: float = Field(..., ge=0, le=1, description="Percentage of deductible. Must be between 0 and 1.")
    broker_fee: float = Field(..., ge=0, description="Fee charged by the broker. Must be greater than or equal to 0.")
    address_street: str = Field(..., min_length=1, description="Street name of the address.")
    address_number: str = Field(..., description="House or building number.")
    address_neighborhood: str = Field(..., description="Neighborhood or district.")
    address_city: str = Field(..., min_length=2, description="City where the address is located.")
    address_state: str = Field(..., min_length=2, max_length=2, description="State code.")
    address_country: str = Field(..., min_length=2, description="Country name.")
    address_postal_code: str = Field(..., min_length=5, max_length=10, description="Postal code.")

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    try:
        return Settings()
    except ValidationError as e:
        error_messages = []
        for error in e.errors():
            field_name = error["loc"][0]
            error_message = error["msg"]
            error_messages.append(f"Error in '{field_name}': {error_message}")

        message = "\n".join(error_messages)
        raise ValueError(f"Configuration validation failed:\n{message}") from e
