from pydantic import BaseModel


class ShipperRequest(BaseModel):
    name: str
    address: str
    cities: str
    state: str
    zipcode: int
    phone_no: int
    email: str
