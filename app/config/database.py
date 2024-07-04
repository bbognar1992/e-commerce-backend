from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import settings

if settings.DEBUG:
    SQLALCHEMY_DATABASE_URL = settings.SQLITE_CONNECTION_STRING
    ASYNC_SQLALCHEMY_DATABASE_URL = settings.POSTGRES_CONNECTION_STRING.replace(
        "sqlite", "sqlite+aiosqlite"
    )
else:
    SQLALCHEMY_DATABASE_URL = settings.POSTGRES_CONNECTION_STRING
    ASYNC_SQLALCHEMY_DATABASE_URL=settings.POSTGRES_CONNECTION_STRING.replace(
        "postgresql", "postgresql+asyncpg"
    )

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
async_engine = create_async_engine(
    ASYNC_SQLALCHEMY_DATABASE_URL,
    echo=False, future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
AsyncSessionLocal = sessionmaker(
    class_=AsyncSession,
    expire_on_commit=False,
    bind=async_engine,
)

Base = declarative_base()


def get_db():
    """
    Create a database session.

    Yields:
        Session: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def async_get_db() -> AsyncSession:
    async_session = AsyncSessionLocal
    async with async_session() as db:
        yield db
