from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.users import crud
from api_v1.users.schemas import CreateUser
from core.models import User, db_helper

router = APIRouter(tags=["Users"])


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)


# @router.get("/")
# async def create_user(
#     user_in: CreateUser,
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency)
# ):
#     return await crud.create_user(session=session, user_in=user_in)
#
