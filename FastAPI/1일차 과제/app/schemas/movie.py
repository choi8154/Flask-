from pydantic import BaseModel
from datetime import date

class Movie(BaseModel):
    title : str
    release_date : date
    rating : float
    country : str


class CreateMovie(Movie):
    director_id : int

class ReadMovie(Movie):
    id : int

    class config:
        orm_mode = True