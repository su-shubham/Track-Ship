from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..repositories.goods_repo import GoodsRepository
from ..db_config.connect import get_session
from ..models.request.goods_req import GoodReq

router = APIRouter(tags=["Goods"])


@router.post("/goods")
async def insert(goods: GoodReq, session: AsyncSession = Depends(get_session)):
    goods = await GoodsRepository(session).insert(**dict(goods))
    return goods
