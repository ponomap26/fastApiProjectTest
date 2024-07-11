from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .dependencis import product_by_id
from .schemas import Product, ProductCreate

router = APIRouter(tags=["products"])


@router.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{products.id}", response_model=Product)
async def get_product(
    product: Product = Depends(product_by_id),
):
    return product
