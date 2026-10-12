
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "postgresql+psycopg://hakansungurlu@localhost:5432/football_blog"

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass
