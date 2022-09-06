from pydantic import BaseModel


class BookModel(BaseModel):
    id: int
    keyword: str
    publisher: str
    price: int
    image: str
