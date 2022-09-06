from typing import List
from fastapi.responses import HTMLResponse
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pathlib import Path

from database import crud
from database import models, schemas
from database.connection import SessionLocal, engine
from book_scraper import NaverBookScraper

models.Base.metadata.create_all(bind=engine)

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

templates = Jinja2Templates(directory=BASE_DIR / "templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.post("/create/book", response_model=schemas.Book)
async def create_book(request: Request, book: schemas.BookCreate, db: Session = Depends(get_db)):

    if db_book is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_book


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "북북이"}
    )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    keyword = q
    keyword = q
    naver_book_scraper = NaverBookScraper()
    books = await naver_book_scraper.search(keyword=keyword, total_page=10)
    for book in books:
        book_model.keyword = keyword
        book_model.price = book['price']
        book_model.publisher = book['publisher']
        book_model.image = book['image']
        # db_book = crud.create_book(db, book_model)
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "q": q}
    )
