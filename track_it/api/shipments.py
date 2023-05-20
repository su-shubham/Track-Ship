from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.shipments_repo import ShipmentRepository
from ..db_config.connect import AsyncSessionFactory, get_session
from ..models.request.shipments_req import ShipmentReq


router = APIRouter(tags=["Shipments"])


@router.post("/shipments")
async def insert_shipment(
    shipment: ShipmentReq, session: AsyncSession = Depends(get_session)
):
    shipment = await ShipmentRepository(session).insert_shipment(shipment)
    return shipment


@router.get("/shipments")
async def get_shipments(shipment: ShipmentReq):
    async with AsyncSessionFactory() as session:
        async with session.begin():
            shipment = await ShipmentRepository(session).get_shipments()
            return shipment
