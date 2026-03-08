from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


# shared fields between all user schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: str = Field(min_length=2, max_length=100)


# schema for creating a user — includes password
class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=50)


# schema for updating a user — all fields optional
class UserUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=2, max_length=100)
    is_active: bool | None = None


# schema for returning a user in response — never includes password
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}  # allows reading from SQLAlchemy model
