from typing import AsyncGenerator

from fastapi_users.models import ID
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[str], Base):
    id: ID
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
