from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .schemas import Product, ProductCreate

router = APIRouter(tags=["products"])


@router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependencies)):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependencies),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{products.id}", response_model=Product)
async def get_products(
    product_id: int, session: AsyncSession = Depends(db_helper.session_dependencies)
):
    product = await crud.get_product(session=session, product_id=product_id)
    if product is None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id {product_id} not found",
    )
