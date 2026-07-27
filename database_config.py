from typing import AsyncGenerator
from dotenv import load_dotenv
import os

load_dotenv()
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
load_dotenv()
DB_URL = os.getenv("DATABASE_URL")
DATABASE_URL: str = DB_URL

engine = create_async_engine(
    DATABASE_URL,
    echo=False, #Used for query logging
    pool_pre_ping=True,
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

