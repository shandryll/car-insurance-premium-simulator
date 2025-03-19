from fastapi import FastAPI

from src.api.controllers.insurance import routes as insurance_routes
from src.config import get_settings
from src.services import health_check

settings = get_settings()

app = FastAPI(
    title="Car Insurance Premium Simulator",
    description="API to calculate car insurance premiums based on a car's age, value, deductible percentage and a broker's fee.",
    version="1.0.0",
)


@app.get("/config/")
async def read_config() -> dict:
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


app.include_router(health_check.router, prefix="/api/v1")
app.include_router(insurance_routes.router, prefix="/api/v1")
