import os
from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """
    Application settings.
    """
    # FastAPI
    # Debug should be set to False on production
    DEBUG: Optional[bool] = os.getenv("DEBUG") == "True"
    # Title is the name of application
    TITLE: Optional[str] = os.getenv("TITLE")

    # SQLITE connection string
    SQLITE_CONNECTION_STRING: Optional[str] = "sqlite:///database.db"

    # PostgreSQL connection string
    POSTGRESS_USER: Optional[str] = os.getenv("POSTGRES_USER")
    POSTGRESS_PASSWORD: Optional[str] = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOSTNAME: Optional[str] = os.getenv("POSTGRES_HOSTNAME", "db")
    POSTGRES_PORT: Optional[int] = int(os.getenv("POSTGRES_PORT", "5432"))
    POSTGRES_DB: Optional[str] = os.getenv("POSTGRES_DB")
    POSTGRES_CONNECTION_STRING: str = f"postgresql://{POSTGRESS_USER}:{POSTGRESS_PASSWORD}@{POSTGRES_HOSTNAME}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # JWT
    SECRET_KEY: Optional[str] = os.getenv("SECRET_KEY")
    ALGORITHM: Optional[str] = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: Optional[int] = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


settings = Settings()
