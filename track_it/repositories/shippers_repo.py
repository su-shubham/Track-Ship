from ..models.data.core_models import Shippers
from sqlalchemy import insert, update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class ShippersRepository:
    def __init__(self, sess: Session) -> None:
        self.sess = sess

    async def insert(self, shipper: Shippers) -> bool:
        try:
            query = insert(Shippers).values(**shipper.dict())
            query.execution_options(synchronize_session="fetch")
            await self.sess.execute(query)
        except Exception as e:
            print(e)
            return e
        return True
