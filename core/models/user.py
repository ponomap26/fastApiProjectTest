from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .post import Post


class User(Base, SQLAlchemyBaseUserTable):
    username: Mapped[str] = mapped_column(String(32))
    posts: Mapped[list["Post"]] = relationship(back_populates="user")
