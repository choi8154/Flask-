from pydantic import BaseModel
from datetime import date
from app.schemas.movie import ReadMovie
from typing import List

class Director(BaseModel):
    name : str
    nationality : str
    birth_date : date
    biography : str

class CreateDirector(Director):
    pass

class ReadDirector(Director):
    id : int
    movies: List[ReadMovie] #readmovie의 객체여야함. 리스트 중첩. 사실 아직 이해 못함...

    class config():
        orm_mode = True