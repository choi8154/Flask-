from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

DB_URL= "mysql+pymysql://root:dain8154@localhost/Movie"

engine = create_engine(DB_URL, echo=True)

Base = declarative_base()

from app.models.director import Director
from app.models.movie import Movie

Base.metadata.create_all(bind=engine)

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()