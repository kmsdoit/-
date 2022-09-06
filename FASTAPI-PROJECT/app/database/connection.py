import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import POSTGRES_DB_NAME,POSTGRES_DB_PORT,POSTGRES_DB_HOST,POSTGRES_DB_USER,POSTGRES_DB_PASSWORD


URL = f"postgresql://{POSTGRES_DB_USER}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}"

engine = create_engine(
    URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
