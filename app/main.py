from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hellow from the fastapi"}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/items/")
def read_query(skip:int = 0, limit:int = 10):
    return {"skip": skip, "limit": limit}

class Item(BaseModel):
    name: str
    role: str

@app.post("/users/")
async def create_user(user: Item):
    modify_user = {"name": user.name.upper(), "role": user.role.upper()}
    return modify_user
