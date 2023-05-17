from fastapi import APIRouter
from ..db_config.connect import AsyncSessionFactory
from ..repositories.trucks_repo import TrucksRepository
from ..models.data.core_models import Trucks
from ..models.request.trucks_req import TruckRequest

router = APIRouter(tags=["Trucks"])


@router.get("/trucks")
async def get_all():
    async with AsyncSessionFactory() as session:
        async with session.begin():
            trucks = await TrucksRepository(session).get_all_trucks()
            return trucks


@router.get("/trucks/{id}")
async def get(id: int):
    async with AsyncSessionFactory() as session:
        async with session.begin():
            truck = await TrucksRepository(session).get_truck(id)
            return truck


@router.post("/trucks")
async def insert(truck: TruckRequest):
    async with AsyncSessionFactory() as session:
        async with session.begin():
            repo = TrucksRepository(session)
            trucks = Trucks(
                license_plate=truck.license_plate,
                manufactured_by=truck.manufactured_by,
                model=truck.model,
                year=truck.year,
                capacity=truck.capacity,
                status=truck.status,
            )
            return await repo.insert_truck(trucks)
