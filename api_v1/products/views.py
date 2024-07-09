from fastapi import APIRouter, HTTPException, status


from . import crud
from .schemas import Product, ProductCreate

router = APIRouter(tars=["Products"])


@router.get("/", responses_model=list[Product])
async def get_products(session):
    return await crud.get_products(session=session)


@router.post("/", responses_model=Product)
async def create_product(session, product_in: ProductCreate):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{products.id}", responses_model=Product)
async def get_products(product_id: int, session):
    product = await crud.get_product(session=session, product_id=product_id)
    if product is None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id {product_id} not found",
    )
