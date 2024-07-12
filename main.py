from contextlib import asynccontextmanager

from core.config import settings
from core.models import Base, db_helper
from api_v1 import router as router_v1
import uvicorn
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Magazine API",
    tags="Magazine",
    lifespan=lifespan,
)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/", tags=["users"])
async def root():
    return {"message": "Hello World"}


#

"""запросы к API"""


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
