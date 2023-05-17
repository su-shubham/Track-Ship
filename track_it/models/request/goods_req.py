from pydantic import BaseModel


class GoodRequest(BaseModel):
    name: str
    description: str
    quantity: int
    weights: int
    value: int
    shipments_id: int
