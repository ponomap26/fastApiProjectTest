from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base


class Category(Base):
    __tablename__ = "categorys"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
