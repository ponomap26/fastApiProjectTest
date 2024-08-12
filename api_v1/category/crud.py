from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.category.schemas import CategoryCreate
from core.models import Category


async def get_all_category(session: AsyncSession):
    stmt = select(Category).order_by(Category.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return products


async def create_category(
    session: AsyncSession, category_in: CategoryCreate
) -> Category:
    category = Category(**category_in.model_dump())
    session.add(category)
    await session.commit()
    # await session.refresh(product)
    return category
