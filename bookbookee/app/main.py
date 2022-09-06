from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
from app.models import postgresdb
from sqlalchemy.orm import Session
from app.models import schemas

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse, response_model=schemas.BookModel)
async def root(request: Request, book: schemas.BookModel, db: Session = Depends(postgresdb.get_db)):
    print(book.keyword)
    # db_book = create_book(db=db, book=book_entity)
    # print(db_book)
    # return templates.TemplateResponse(
    #     "./index.html",
    #     {"request": request, "title": "콜렉터 북북이"}
    # )


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    print(q)
    return templates.TemplateResponse(
        "./index.html",
        {"request": request, "title": "콜렉터 북북이", "keyword": q}
    )


@app.on_event("startup")
async def on_app_start():
    postgresdb.connect()
    print("DB 접속 성공")


@app.on_event("shutdown")
async def on_app_shutdown():
    postgresdb.disconnect()
    print("DB 접속 종료")
