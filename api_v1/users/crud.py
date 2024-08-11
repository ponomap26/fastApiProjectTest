from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.users.schemas import UserCreate
from core.models import User


async def get_user(session: AsyncSession) -> list[User]:
    stms = select(User).order_by(User.id)
    result: Result = await session.execute(stms)
    users = result.scalars().all()
    return list(users)


async def get_users(session: AsyncSession, user_id: int) -> User | None:
    return await session.get(User, user_id)


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user
