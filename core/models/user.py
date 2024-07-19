from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base, SQLAlchemyBaseUserTable):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pass
