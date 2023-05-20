from ..models.data.core_models import Shipments
from sqlalchemy import insert, update, delete
from sqlalchemy.future import select
from sqlalchemy.orm import Session


class ShipmentRepository:
    def __init__(self, sess: Session) -> None:
        self.sess = sess

    async def insert_shipment(self, shipment: Shipments) -> bool:
        try:
            query = insert(Shipments).values(**shipment.dict())
            query.execution_options(synchronize_session="fetch")
            await self.sess.execute(query)
        except Exception as e:
            return e
        return True
