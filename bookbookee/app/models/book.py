from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from app.models import postgresdb

Base = declarative_base()


class Book(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    keyword: Column(String)
    publisher: Column(String)
    price: Column(Integer)
    image: Column(String)


Base.metadata.create_all(bind=postgresdb.engine)
