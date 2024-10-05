from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from pydantic import EmailStr
from sqlalchemy import String, Integer, Boolean

from sqlalchemy.orm import Mapped, mapped_column, relationship


from core.models.base import Base

if TYPE_CHECKING:
    from .post import Post
    from .profile import Profile
    from core.models.modelProduct.product import Product


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(
        String(length=320), unique=True, nullable=False
    )
    email: Mapped[EmailStr] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    posts: Mapped["Post"] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")
    products: Mapped["Product"] = relationship(back_populates="user")
