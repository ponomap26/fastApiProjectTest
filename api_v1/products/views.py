from fastapi import APIRouter, status
from fastapi.params import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .dependencis import product_by_id
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial

router = APIRouter(tags=["products"])

"""
Получить все продукты
"""


@router.get("/", response_model=list[Product])
async def get_all_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Этот конечный пункт возвращает все продукты.
    """
    return await crud.get_all_products(session=session)


"""
Создать новый продукт
"""


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Этот конечный пункт создает новый продукт.
    """
    return await crud.create_product(session=session, product_in=product_in)


"""
Получить конкретный продукт по ID
"""


@router.get("/{products_id}", response_model=Product)
async def get_product(
    product: Product = Depends(product_by_id),
):
    """
    Этот конечный пункт возвращает продукт по его ID.
    """
    return product


"""
Обновить продукт по ID
"""


@router.put("/{products_id}", response_model=Product)
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Этот конечный пункт обновляет продукт по его ID.
    """
    return await crud.update_product(
        session=session, product=product, product_update=product_update
    )


"""
Частично обновить продукт по ID
"""


@router.patch("/{product_id}/")
async def update_product_partial(
    product_update: ProductUpdatePartial,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    """
    Этот конечный пункт частично обновляет продукт по его ID.
    """
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True,
    )


"""
Удалить продукт по ID
"""


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    """
    Этот конечный пункт удаляет продукт по его ID.
    """
    await crud.delete_product(session=session, product=product)
