from pydantic import BaseModel


class GoodReq(BaseModel):
    name: str
    description: str
    quantity: int
    weights: int
    value: int
    shipments_id: int
