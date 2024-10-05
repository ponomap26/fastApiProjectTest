from fastapi import APIRouter, Depends, status


from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.auch.users import crud
from api_v1.auch.users.schemas import UserCreate, User
from core.models import db_helper

router = APIRouter(tags=["Users"])


# @router.post("/")
# def create_user(user: UserCreate):
#     return crud.create_user(user_in=user)


@router.get("/", response_model=list[User])
async def get_user(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_user(session=session)


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(session=session, user_in=user_in)
