import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .settings import settings

logger = logging.getLogger()
print("!!!!!!!!!!!")

if settings.DEBUG:
    SQLALCHEMY_DATABASE_URL = settings.SQLITE_CONNECTION_STRING
else:
    SQLALCHEMY_DATABASE_URL = settings.POSTGRES_CONNECTION_STRING

logger.debug(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
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
