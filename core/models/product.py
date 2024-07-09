from sqlalchemy.orm import Mapped, mapped_column, declared_attr

from .base import Base


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str]
    description: Mapped[str]
    prise: Mapped[int]
