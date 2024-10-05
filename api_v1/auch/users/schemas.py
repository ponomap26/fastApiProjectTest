from fastapi_users import schemas, models
from pydantic import EmailStr

from api_v1.auch.auch import password_hash


class User(schemas.BaseUser[int]):
    id: int
    username: str
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    id: int
    email: EmailStr
    username: str
    password: str = password_hash
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
