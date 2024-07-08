from fastapi import FastAPI

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "change_name",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(openapi_tags=tags_metadata, title="Magazine API", tags="Magazine")

fake_data = [
    {"id": 1, "role": "admin", "name": "John Doe"},
    {"id": 2, "role": "user", "name": "Jane Doe"},
    {"id": 3, "role": "user", "name": "Jane Doe"},
]


@app.get("/", tags=["users"])
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{user_id}", tags=["users"])
async def say_hello(user_id: int):
    return [user for user in fake_data if user.get("id") == user_id]


@app.get("/users", tags=["change_name"])
def get_trades(limit: int = 1, offset: int = 0):
    return fake_data[offset:][:limit]


fake_users = [
    {"id": 1, "role": "admin", "name": "John Doe"},
    {"id": 2, "role": "user", "name": "Jane Doe"},
    {"id": 3, "role": "user", "name": "Jane Doe"},
]


@app.post("/user/{user_id})", tags=["change_name"])
def change_user_name(user_id: int, new_name: str):
    curent_user = list(filter(lambda user: user.get("id") == user_id, fake_users))[0]
    curent_user["name"] = new_name
    return {"status": 200, "data": curent_user}
