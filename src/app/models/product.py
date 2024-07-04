import uuid
from datetime import datetime

from sqlalchemy import String, Column, func, DateTime, Text, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from ..config.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, unique=True, index=True)
    summery = Column(Text)
    price = Column(Float)

    created_at: Mapped[datetime] = Column(DateTime, default=func.now())
    updated_at: Mapped[datetime | None] = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at: Mapped[datetime | None] = Column(DateTime, default=None)
    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)
