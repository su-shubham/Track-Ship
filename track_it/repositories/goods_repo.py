from ..models.data.core_models import Goods
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import insert, update, delete


class GoodsRepository:
    def __init__(self, sess: Session) -> None:
        self.sess = sess

    async def insert(self, goods: Goods) -> bool:
        try:
            query = insert(Goods).values(**goods.dict())
            query.execution_options(synchronize_session="fetch")
            await self.sess.execute(query)
        except Exception as e:
            return e
        return True

    async def get(self, id: int) -> bool:
        try:
            query = select(Goods).where(Goods.id == id)
            reuslt = await self.sess.execute(query)
            return reuslt.scalars().first()
        except Exception as e:
            return e
