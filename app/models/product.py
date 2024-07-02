import uuid

from sqlalchemy import String, Column, func, DateTime, Text, Float
from sqlalchemy.dialects.postgresql import UUID
from config.database import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True, index=True)
    summery = Column(Text)
    price = Column(Float)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
