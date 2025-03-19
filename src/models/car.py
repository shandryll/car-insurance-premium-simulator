from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class ICar(BaseModel):
    make: str = Field(..., min_length=1, description="The manufacturer of the car. Cannot be empty.")
    model: str = Field(..., min_length=1, description="The model of the car. Cannot be empty.")
    year: int = Field(..., ge=1886, description="The year of the car. Must be 1886 or later.")
    value: float = Field(..., gt=0, description="The value of the car. Must be greater than zero.")

    @field_validator("year")
    def validate_year(cls, value: int) -> int:
        current_year = datetime.now().year
        if value > current_year:
            raise ValueError(f"The year must be less than or equal to {current_year}.")
        return value
