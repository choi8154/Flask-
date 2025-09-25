from . import Base 
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship



################BD 테이블 생성#################
class User(Base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True, index=True)
    login_id = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    phone = Column(String(50), unique=True, nullable=True)
############################################