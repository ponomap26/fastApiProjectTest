from contextlib import asynccontextmanager

from core.config import settings


from api_v1 import router as router_v1

import uvicorn
from fastapi import FastAPI

from core.models import db_helper, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(
    title="Magazine API",
    tags="Magazine",
    lifespan=lifespan,
)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)

#

"""запросы к API"""


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
