from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship


################BD 테이블 생성#################
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id") ,nullable=False)
    category = Column(String(30), nullable=True)
    title = Column(String(200), nullable=False)
    content = Column(String(1000), nullable=False)
    # author = relationship("User", back_populates="boards")
    create_at = Column(DateTime, server_default=func.now(), nullable=False) #자동으로 시간 생성
############################################