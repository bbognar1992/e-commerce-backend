from typing import Optional

from pydantic import BaseModel, UUID4, field_validator

from ..auth.email_validator import validate_email
from ..auth.password_validator import validate_password


class UserBase(BaseModel):
    email: str
    username: str
    is_superuser: bool = False
    is_active: bool = True


class UserIn(UserBase):
    password: str

    @field_validator('password')
    def passwords_match(cls, v):
        validate_password(v)
        return v

    @field_validator('email')
    def email_match(cls, v):
        validate_email(v)
        return v


class UserInDBBase(UserBase):
    id: UUID4

    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    hashed_password: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str