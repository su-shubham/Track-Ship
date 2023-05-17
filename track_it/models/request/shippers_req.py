from pydantic import BaseModel


class ShipperRequest(BaseModel):
    name: str
    address: str
