from pydantic import BaseModel


class ShipmentReq(BaseModel):
    id: int
    shipment_date: str
    origin: str
    destination: str
    truck_id: int
    driver_id: int
    shipper_id: int
    date: str
