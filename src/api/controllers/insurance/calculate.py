from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/v1/calculate")
def calculate(data: Request) -> JSONResponse:
    """."""
    return {"status": "ok"}
