from ..models.data.core_models import Trucks
from sqlalchemy import insert, update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class TrucksRepository:
    def __init__(self, sess: Session):
        self.sess = sess

    async def insert_truck(self, truck: Trucks) -> bool:
        try:
            query = insert(Trucks).values(
                license_plate=truck.license_plate,
                manufactured_by=truck.manufactured_by,
                model=truck.model,
                year=truck.year,
                capacity=truck.capacity,
                status=truck.status,
            )
            query.execution_options(synchronize_session="fetch")
            await self.sess.execute(query)
        except Exception as e:  # noqa: E722
            return e
        return True

    async def update_truck(self, id: int, details: dict[str, any]) -> bool:
        try:
            query = update(Trucks).where(Trucks.id == id).values(**details)
            query.execution_options(synchronize_session="fetch")
            await self.sess.execute(query)
        except:  # noqa: E722
            return False
        return True

    async def remove_truck(self, id: int) -> bool:
        try:
            query = delete(Trucks).where(Trucks.id == id)
            query.execution_options(synchronize_session="fetch")
            await self.sess.execute(query)
        except:  # noqa: E722
            return False
        return True

    async def get_all_trucks(self):
        try:
            query = await self.sess.execute(select(Trucks))
            return query.scalars().all()
        except:  # noqa: E722
            return {"message": "Not Found"}

    async def get_truck(self, id: int):
        try:
            query = await self.sess.execute(select(Trucks).where(Trucks.id == id))
            return query.scalars().all()
        except:  # noqa: E722
            return {"message": f"Truck with id {id} not found"}

    async def truck_status(self, id: int) -> dict[bool, Trucks]:
        try:
            query = await self.sess.execute(select(Trucks).where(Trucks.status == True))
            if query.scalars().all():
                return {"status": True, "truck": query.scalars.all()}
            return False
        except:  # noqa: E722
            return {"message": f"Truck with id {id} is not available"}
