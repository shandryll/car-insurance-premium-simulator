from fastapi import FastAPI

from src.application.services import config_check, health_check
from src.infrastructure.controllers.insurance import routes as insurance_routes

app = FastAPI(
    title="Car Insurance Premium Simulator",
    description="API to calculate car insurance premiums based on a car's age, value, deductible percentage and a broker's fee.",
    version="1.0.0",
)


app.include_router(health_check.router, prefix="/api/v1")
app.include_router(config_check.router, prefix="/api/v1")
app.include_router(insurance_routes.router, prefix="/api/v1")
