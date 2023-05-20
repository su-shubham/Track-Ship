from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = "postgresql+asyncpg://postgres:root@localhost:5432/DriveIt"
engine = create_async_engine(DB_URL, echo=True, future=True)
AsyncSessionFactory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()


async def get_session():
    async with AsyncSessionFactory() as session:
        async with session.begin():
            yield session
