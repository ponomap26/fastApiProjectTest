from contextlib import asynccontextmanager

from core.config import settings
from core.models import Base, db_helper
from api_v1 import router as router_v1
import uvicorn
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(
    title="Magazine API",
    tags="Magazine",
    lifespan=lifespan,
)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

# fake_data = [
#     {"id": 1, "role": "admin", "name": "John Doe"},
#     {"id": 2, "role": "user", "name": "Jane Doe"},
#     {"id": 3, "role": "user", "name": "Jane Doe"},
# ]


@app.get("/", tags=["users"])
async def root():
    return {"message": "Hello World"}


# @app.get("/hello/{user_id}", tags=["users"])
# async def say_hello(user_id: int):
#     return [user for user in fake_data if user.get("id") == user_id]

#
# @app.get("/users", tags=["change_name"])
# def get_trades(limit: int = 1, offset: int = 0):
#     return fake_data[offset:][:limit]
#
#
# fake_users = [
#     {"id": 1, "role": "admin", "name": "John Doe"},
#     {"id": 2, "role": "user", "name": "Jane Doe"},
#     {"id": 3, "role": "user", "name": "Jane Doe"},
# ]

"""запросы к API"""


# @app.post("/user/{user_id})", tags=["change_name"])
# def change_user_name(user_id: int, new_name: str):
#     curent_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
#     curent_user["name"] = new_name
#     return {"status": 200, "data": curent_user}


if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8080)
