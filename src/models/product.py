from typing import Optional

from pydantic import BaseModel


class IProduct(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    price: float
    quantity: Optional[int] = 0
