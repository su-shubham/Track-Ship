from ..models.data.core_models import Drivers
from sqlalchemy import insert, update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from ..models.request.drivers_req import DriverUpdateReq


class DriversRepository:
    def __init__(self, sess: Session):
        self.sess = sess

    async def insert_driver(self, driver: Drivers) -> bool:
        try:
            query = insert(Drivers).values(**driver.dict())
            query.execution_options(synchronize_session="fetch")
            await self.sess.execute(query)
        except Exception as e:  # noqa: E722
            return e
        return True

    async def get_all(self):
        try:
            query = await self.sess.execute(select(Drivers))
            return query.scalars().all()
        except:
            return {"message": "Not Found"}

    async def get_one(self, id: int):
        try:
            query = await self.sess.execute(select(Drivers).where(Drivers.id == id))
            return query.scalars().all()
        except:
            return {"message": "Something went wrong"}

    async def update_driver(self, id: int, details: DriverUpdateReq):
        try:
            query = update(Drivers).where(Drivers.id == id).values(**details)
            if query is None:
                return {"message": f"Driver with id {id} not found"}
            query.execution_options(synchronize_session="fetch")
            updated = await self.sess.execute(query)
            if updated:
                return {"message": f"Driver with id {id} updated"}
            else:
                return {"message": "Something went wrong"}
        except Exception as e:  # noqa: E722
            return e

    async def delete_driver(self, id: int):
        try:
            query = delete(Drivers).where(Drivers.id == id)
            query.execution_options(synchronize_session="fetch")
            await self.sess.execute(query)
        except Exception as e:  # noqa: E722
            return e

    async def get_truck_driver(self, id: int):
        try:
            query = await self.sess.execute(
                select(Drivers).where(Drivers.truck_id == id)
            )
            return query.scalars().first()
        except:
            return {"message": "Something went wrong"}
