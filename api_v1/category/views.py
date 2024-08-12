from fastapi import APIRouter, status
from fastapi.params import Depends


from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper
from .schemas import Category, CategoryCreate

router = APIRouter(tags=["categorys"])


@router.get("/", response_model=list[Category])
async def get_all_category(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_all_category(session=session)


@router.post("/", response_model=Category, status_code=status.HTTP_201_CREATED)
async def create_category(
    category_in: CategoryCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.create_category(session=session, category_in=category_in)
