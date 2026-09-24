from typing import TypedDict

class OrderState(TypedDict):
    product: str
    quantity: int
    is_valid: bool
    stock_available: bool
    status: str