from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from core.models.modelUsers.user import User


class UserRelationMixin:
    _user_id_nullable: bool = False
    _user_id_unique: bool = True
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("user_table.id"),
            unique=cls._user_id_unique,
        )

    @declared_attr
    def user_id(cls) -> Mapped["User"]:
        return relationship(
            "User",
            back_populates=cls._user_back_populates,
        )
