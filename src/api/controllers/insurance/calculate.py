from fastapi import APIRouter

router = APIRouter()


@router.get("/v1/calculate")
def health() -> dict[str, str]:
    """."""
    return {"status": "ok"}
