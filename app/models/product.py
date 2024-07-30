from typing import Optional
from .common_model import CommonModel


class Product(CommonModel):
    name: str
    description: str
    price: Optional[float] = 0.00


class UpdateProduct(CommonModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float] = 0.00