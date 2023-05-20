from fastapi import APIRouter, Depends
from ..repositories.shippers_repo import ShippersRepository
from ..db_config.connect import AsyncSessionFactory, get_session
from ..models.request.shippers_req import ShipperRequest

router = APIRouter(tags=["Shippers"])


@router.post("/shippers")
async def insert_shipper(
    shipper: ShipperRequest, session: AsyncSessionFactory = Depends(get_session)
):
    shipper = await ShippersRepository(session).insert(shipper)
    return shipper
