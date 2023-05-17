from ..models.data.core_models import Drivers
from sqlalchemy import insert, update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class DriversRepository:
    def __init__(self, sess: Session):
        self.sess = sess

    async def insert_driver(self, driver: Drivers) -> bool:
        try:
            query = insert(Drivers).values(
                name=driver.name,
                license_number=driver.license_number,
                address=driver.address,
                city=driver.city,
                state=driver.state,
                zipcode=driver.zipcode,
                phone_no=driver.phone_no,
                email=driver.email,
                truck_id=driver.truck_id,
            )
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
        
    async def get_one(self,id:int):
        try:
            query = await self.sess.execute(select(Drivers).where(Drivers.id == id))
            return query.scalars().all()
        except:
            return {"message": f"Driver with id {id} not found"}    

    async def get_shipments(self,id:int):
        try:
            query = await self.sess.execute(select(Drivers).where(Drivers.id == id))
            return query.scalars().all()
        except:
            return {"message": f"Driver with id {id} not found"}