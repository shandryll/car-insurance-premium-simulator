from fastapi import FastAPI

from src.api.controllers.insurance import calculate
from src.services import health_check

app = FastAPI(
    title="Car Insurance Premium Simulator",
    description="API to calculate car insurance premiums based on a car's age, value, deductible percentage and a broker's fee.",
    version="1.0.0",
)

app.include_router(health_check.router, prefix="/api/v1")
app.include_router(calculate.router, prefix="/api/v1")
