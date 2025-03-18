from pydantic import BaseModel, Field


class ICar(BaseModel):
    make: str = Field(..., min_length=1, description="The manufacturer of the car. Cannot be empty.")
    model: str = Field(..., min_length=1, description="The model of the car. Cannot be empty.")
    year: int = Field(..., ge=1886, description="The year of the car. Must be 1886 or later.")
    value: float = Field(..., gt=0, description="The value of the car. Must be greater than zero.")
