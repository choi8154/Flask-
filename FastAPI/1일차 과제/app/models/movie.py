from sqlalchemy import Integer, Column, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import relationship
from . import Base

class Movie(Base):
    __tablename__="movie"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(100), nullable=False)
    release_date = Column(Date, nullable=False)
    rating = Column(DECIMAL(3,2), nullable=False)
    country = Column(String(100), nullable=False)
    director_id = Column(Integer, ForeignKey("director.id"))
    director = relationship("User", back_populates="movies")