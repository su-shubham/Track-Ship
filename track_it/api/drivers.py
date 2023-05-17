from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..db_config.connect import AsyncSessionFactory
from ..repositories.drivers_repo import DriversRepository
from ..models.data.core_models import Drivers
from ..models.request.drivers_req import DriverReq, Drivers

router = APIRouter(tags=["Drivers"])


@router.post("/drivers")
async def insert(driver: DriverReq):
    async with AsyncSessionFactory() as session:
        async with session.begin():
            repo = DriversRepository(session)
            drivers = Drivers(**dict(driver))
            return await repo.insert_driver(drivers)


@router.get("/drivers", response_class=JSONResponse)
async def get_all():
    async with AsyncSessionFactory() as session:
        async with session.begin():
            repo = DriversRepository(session)
            return await repo.get_all()


@router.get("/drivers/{id}")
async def get_one(id: int):
    async with AsyncSessionFactory() as session:
        async with session.begin():
            repo = DriversRepository(session)
            return await repo.get_one(id)

@router.get("/drivers/{id}/shipments")
async def get_shipments(id: int):
    async with AsyncSessionFactory() as session:
        async with session.begin():
            repo = DriversRepository(session)
            return await repo.get_shipments(id)