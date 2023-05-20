from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from ..db_config.connect import get_session
from ..repositories.drivers_repo import DriversRepository
from ..models.data.core_models import Drivers
from ..models.request.drivers_req import DriverReq, Drivers, DriverUpdateReq
from sqlalchemy.ext.asyncio import AsyncSession
from ..exceptions import ShipException

router = APIRouter(tags=["Drivers"])


@router.post("/drivers")
async def insert(driver: DriverReq, session: AsyncSession = Depends(get_session)):
    repo = DriversRepository(session)
    drivers = Drivers(**dict(driver))
    return await repo.insert_driver(drivers)


@router.get("/drivers", response_class=JSONResponse)
async def get_all(session: AsyncSession = Depends(get_session)):
    repo = DriversRepository(session)
    return await repo.get_all()


@router.get("/drivers/{id}")
async def get_one(id: int, session: AsyncSession = Depends(get_session)):
    repo = DriversRepository(session)
    result = await repo.get_one(id)
    if result:
        return result
    else:
        return ShipException(404, f"Driver with id {id} not found. Register First!!!!")


@router.patch("/drivers/update")
async def update(
    id: int, driverReq: DriverUpdateReq, session: AsyncSession = Depends(get_session)
):
    repo = DriversRepository(session)
    dict = driverReq.dict(exclude_unset=True)
    return await repo.update_driver(id, dict)


@router.delete("/drivers/{id}")
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    repo = DriversRepository(session)
    return await repo.delete_driver(id)


@router.get("/drivers/{id}/truck")
async def get_truck_driver(id: int, session: AsyncSession = Depends(get_session)):
    repo = DriversRepository(session)
    result = await repo.get_truck_driver(id)
    if result:
        return JSONResponse(
            content=f"Driver with id {result.id} is assigned to a truck",
            status_code=200,
        )
    else:
        return ShipException(404, f"Driver with id {id} not found. Register First!!!!")
