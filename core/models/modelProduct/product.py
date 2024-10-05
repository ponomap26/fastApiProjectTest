from typing import TYPE_CHECKING


from sqlalchemy.orm import relationship


from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column


from core.models import Base


class Product(Base):

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)  # добавил nullable
    description: Mapped[str] = mapped_column(String, nullable=True)  # добавил nullable
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    price: Mapped[float] = mapped_column(Float, nullable=False)  # добавил nullable
    cat_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("categorys.id"), nullable=False
    )  # изменил тип
    creator: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), nullable=False
    )  # изменил тип
    category = relationship("Category", back_populates="products")
    user = relationship("User", back_populates="products")
