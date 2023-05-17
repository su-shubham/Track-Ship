from pydantic import BaseModel


class TruckRequest(BaseModel):
    license_plate: str
    manufactured_by: str
    model: int
    year: int
    capacity: int
    status: bool
