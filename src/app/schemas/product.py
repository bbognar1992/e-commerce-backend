import uuid
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field, PositiveFloat, ConfigDict


class ProductBase(BaseModel):
    title: Annotated[str, Field(min_length=2, max_length=50,
                                examples=["This is the product title"])]
    summery: Annotated[str, Field(min_length=1, max_length=63206,
                                  examples=["This is the product summary"])]
    price: PositiveFloat


class ProductCreate(ProductBase):
    model_config = ConfigDict(extra="forbid")

    title: Annotated[str, Field(min_length=2, max_length=50,
                                examples=["This is the product title"])]
    summery: Annotated[str, Field(min_length=1, max_length=63206,
                                  examples=["This is the product summary"])]
    price: PositiveFloat


class ProductRead(ProductBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class ProductUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: Annotated[str | None, Field(min_length=2, max_length=50,
                                       examples=["This is the product title"])]
    summery: Annotated[str | None, Field(min_length=1, max_length=63206,
                                         examples=[
                                             "This is the product summary"])]
    price: PositiveFloat | None


class ProductUpdateInternal(ProductUpdate):
    updated_at: datetime


class ProductDelete(BaseModel):
    model_config = ConfigDict(extra="forbid")

    is_deleted: bool
    deleted_at: datetime
