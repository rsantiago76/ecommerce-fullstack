from pydantic import BaseModel, Field

class ProductOut(BaseModel):
    id: int
    sku: str
    name: str
    description: str
    price: float
    image_url: str

class CartItemIn(BaseModel):
    product_id: int
    quantity: int = Field(default=1, ge=1, le=99)

class CartItemOut(BaseModel):
    id: int
    product_id: int
    quantity: int
    product: ProductOut

class CartOut(BaseModel):
    items: list[CartItemOut]
    subtotal: float

class CheckoutOut(BaseModel):
    mode: str
    checkout_url: str | None = None
    message: str
