from typing import Optional

from pydantic import BaseModel, Field


class IAddress(BaseModel):
    street: str = Field(..., min_length=1, description="Street name of the address.")
    number: str = Field(..., description="House or building number.")
    neighborhood: str = Field(..., description="Neighborhood or district.")
    city: str = Field(..., min_length=2, description="City where the address is located.")
    state: str = Field(..., min_length=2, max_length=2, description="State code.")
    country: str = Field(..., min_length=2, description="Country name.")
    postal_code: str = Field(..., min_length=5, max_length=10, description="Postal code.")
    latitude: Optional[float] = Field(ge=-90, le=90, description="Geographical latitude. Must be between -90 and 90.")
    longitude: Optional[float] = Field(ge=-180, le=180, description="Geographical longitude. Must be between -180 and 180.")
