from pydantic import BaseModel
from typing import List, Union

class Providers(BaseModel):
  providers: List[str]

class Product(BaseModel):
    name: str
    image_url: str
    price_amount: Union[int, None]

class Products(BaseModel):
  products: List[Product]
