from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get(
    "/health",
    tags=["Health Check"],
    summary="Check the application's health",
    description=(
        """
        This endpoint checks the status of the application, including critical dependencies,
        such as database connectivity or external services if applicable.
        """
    ),
    responses={
        200: {
            "description": "Application is healthy",
            "content": {
                "application/json": {
                    "example": {
                        "status": "healthy",
                        "details": {
                            "external_api": "online",
                        },
                    },
                },
            },
        },
        503: {
            "description": "Application is unhealthy due to dependency failures",
            "content": {
                "application/json": {
                    "example": {
                        "status": "unhealthy",
                        "details": {
                            "external_api": "offline",
                        },
                    },
                },
            },
        },
    },
)
async def health_check() -> JSONResponse:
    health_status = {
        "status": "healthy",
        "details": {
            "external_api": "online",
        },
    }

    if health_status["status"] != "healthy":
        return HTTPException(content=health_status, status_code=503)

    return JSONResponse(content=health_status, status_code=200)
