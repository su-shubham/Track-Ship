from fastapi import APIRouter, Depends
from ..db_config.connect import AsyncSessionFactory, get_session
from ..repositories.trucks_repo import TrucksRepository
from ..models.data.core_models import Trucks
from ..models.request.trucks_req import TruckRequest
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["Trucks"])


@router.get("/trucks")
async def get_all(session: AsyncSession = Depends(get_session)):
    trucks = await TrucksRepository(session).get_all_trucks()
    return trucks


@router.get("/trucks/{id}")
async def get(id: int, session: AsyncSession = Depends(get_session)):
    truck = await TrucksRepository(session).get_truck(id)
    return truck


@router.post("/trucks")
async def insert(truck: TruckRequest, session: AsyncSession = Depends(get_session)):
    repo = TrucksRepository(session)
    res = Trucks(**dict(truck))
    return await repo.insert_truck(res)


@router.patch("/trucks/")
async def update(
    id: int, truck: TruckRequest, session: AsyncSession = Depends(get_session)
):
    repo = TrucksRepository(session)
    dict = truck.dict(exclude_unset=True)
    return await repo.update_truck(id, dict)


@router.delete("/trucks/{id}")
async def delete(id: int, session: AsyncSession = Depends(get_session)):
    repo = TrucksRepository(session)
    return await repo.remove_truck(id)


# @router.get("/trucks/status")
# async def status(id: int):
#     async with AsyncSessionFactory() as session:
#         async with session.begin():
#             trucks = await TrucksRepository(session).truck_driver(id)
#             return trucks
