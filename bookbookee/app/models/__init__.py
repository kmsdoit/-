from app.config import POSTGRES_DB_HOST, POSTGRES_DB_PORT, POSTGRES_DB_NAME, POSTGRES_DB_PASSWORD, POSTGRES_DB_USER
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_DB_USER}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


class PostgresDB:
    def __init__(self):
        self.engine = None
        self.sessionLocal = None

    def connect(self):
        self.sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def disconnect(self):
        sessionmaker(autocommit=False, autoflush=False, bind=self.engine).close_all()

    def get_db(self):
        db = self.sessionLocal()
        try:
            yield db
        finally:
            db.close()


postgresdb = PostgresDB()
