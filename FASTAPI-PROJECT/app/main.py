from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}


class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: str):
    return fake_db.get(item_id, None)
