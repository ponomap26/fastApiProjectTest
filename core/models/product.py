from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .category import Category
from .base import Base


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    cat_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="products")
