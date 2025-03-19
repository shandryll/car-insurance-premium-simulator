from typing import Optional

from pydantic import BaseModel, Field

from src.domain.entities.address import IAddress
from src.domain.entities.car import ICar


class InsuranceInputDTO(BaseModel):
    car: ICar = Field(..., description="Details of the car associated with the insurance.")
    deductible_percentage: float = Field(..., ge=0, le=1, description="Percentage of deductible. Must be between 0 and 1.")
    broker_fee: float = Field(..., ge=0, description="Fee charged by the broker. Must be greater than or equal to 0.")
    registration_location: Optional[IAddress] = Field(description="Details of the registration location.")


class InsuranceOutputDTO(BaseModel):
    car: ICar = Field(..., description="Details of the car associated with the insurance.")
    applied_rate: float = Field(..., description="Final calculated rate after adjustments.")
    policy_limit: float = Field(..., description="Final policy limit after deductible application.")
    calculated_premium: float = Field(..., description="Final premium after deductible and broker fee adjustments.")
    deductible_value: float = Field(..., description="Monetary value calculated from the original policy limit and deductible percentage.")
