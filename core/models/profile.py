from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .user import User
from .base import Base
from .mixins import UserRelationMixin


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"
    username: Mapped[str | None] = mapped_column(String(32))
    last_name: Mapped[str | None] = mapped_column(String(32))
    bio: Mapped[str | None] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="profile")
