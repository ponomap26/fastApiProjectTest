from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from api_v1.products.schemas import ProductCreate
from core.models import Product, product


"""Create
 Read
 Update
 Delete"""


async def get_products(session: AsyncSession) -> list(Product):
    stms = select(Product).order_by(Product.id)
    result: Result = await session.execute(stms)
    products = result.scalar().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product
