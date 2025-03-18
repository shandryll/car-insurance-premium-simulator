# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse

# app = FastAPI()


# @app.post("/example")
# async def example_endpoint(request: Request):
#     data = await request.json()  # Acessando o corpo da requisição
#     return JSONResponse(content={"message": f"Recebido: {data}"}, status_code=200)



"deductible_percentage": 0.10,
            "broker_fee": 50.0,
            "registration_location": {
                "street": "Main Street",
                "number": "123",
                "city": "New York",
                "state": "NY",
                "country": "USA",
                "postal_code": "10001",
            },
             "make": "Toyota",
            "model": "Corolla",
            "year": 2020,
            "value": 20000.0


import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_read_root():
    """
    Test the root endpoint '/'.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

@pytest.mark.asyncio
async def test_read_item():
    """
    Test the '/items/{item_id}' endpoint with a valid item_id and query parameter.
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/items/42?q=test_query")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test_query"}
