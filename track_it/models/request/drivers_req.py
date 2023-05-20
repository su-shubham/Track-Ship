from pydantic import BaseModel


class Drivers(BaseModel):
    name: str
    license_number: str
    address: str
    city: str
    state: str
    zipcode: int
    phone_no: int
    email: str
    truck_id: int


class DriverUpdateReq(BaseModel):
    name: str
    address: str
    city: str
    state: str
    zipcode: int


class DriverReq(Drivers):
    pass
