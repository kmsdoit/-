from sqlalchemy.orm import Session
from . import book,schemas


def create_book(db: Session, books: schemas.BookModel):
    db_book = book.Book(keyword=books.keyword, publisher=books.publisher, price=books.price, image=books.image)
    db.add(db_book)
    db.commit()
    return db_book
