from sqlalchemy import Integer, Column, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from . import Base

class Director(Base):
    __tablename__="director"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    nationality = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=False)
    biography = Column(String(1000), nullable= True)
    movies = relationship("Movie", back_populates="director")