from ..models.data.core_models import Trucks, Drivers
from sqlalchemy import insert, update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class TrucksRepository:
    def __init__(self, sess: Session):
        self.sess = sess

    async def insert_truck(self, truck: Trucks) -> bool:
        try:
            query = insert(Trucks).values(**truck.dict())
            query.execution_options(synchronize_session="fetch")
            await self.sess.execute(query)
        except Exception as e:  # noqa: E722
            return e
        return True

    async def update_truck(self, id: int, details: dict[str, any]) -> bool:
        try:
            query = update(Trucks).where(Trucks.id == id).values(**details)
            if query is None:
                return {"message": f"Truck with id {id} not found"}
            query.execution_options(synchronize_session="fetch")
            await self.sess.execute(query)
            return {"message": f"Truck with id {id} updated"}
        except:  # noqa: E722
            return False

    async def remove_truck(self, id: int) -> bool:
        try:
            query = delete(Trucks).where(Trucks.id == id)
            if query is None:
                query.execution_options(synchronize_session="fetch")
                return {"message": f"Truck with id {id} not found"}
            await self.sess.execute(query)
        except Exception as e:  # noqa: E722
            return e

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

    async def truck_driver(self, id: int):
        try:
            return self.sess.execute(select(Trucks).where(Trucks.id == id))
        except Exception as e:
            return e
