from pydantic import BaseModel, ConfigDict


class CategioryBase(BaseModel):
    name: str


class CategoryCreate(CategioryBase):
    pass


class Category(CategioryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
