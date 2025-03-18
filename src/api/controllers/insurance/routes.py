from fastapi import APIRouter

router = APIRouter()


@router.get("/calculate")
def health() -> dict[str, str]:
    """."""
    return {"status": "ok"}
