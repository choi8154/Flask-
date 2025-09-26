from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker


# DB생성할 테이블 클레스가 상속
Base = declarative_base()

###################BD 생성###################
# Mysql에 root 계정으로 접속(db 생성시 db이름 붙이지 않음)
engine = create_engine("mysql+pymysql://root:dain8154@localhost")

# DB 생성 db생성 로직은 sqlalchemy에 없으므로 직접 pymysql로 mysql에 접근하여 sql문으로 생성해야함.
with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS blogdb"))
############################################

###################BD 연결###################
# 생성한 DB에 연결
engine = create_engine("mysql+pymysql://root:dain8154@localhost/blogdb")

############################################

# 세션 생성 : 이걸 사용하여 테이블에 데이터를 넣을 수 있음. pymysql에서 cur같은거
SessionLocal = sessionmaker(bind=engine)

#! 순환참조 오류로 밑으로 내려야함.
from .user import User #똑같이 못찾아서 . 붙임
from .post import Post #똑같이 못찾아서 . 붙임

# 테이블 생성
Base.metadata.create_all(engine)


# !!!!순서중요!!!!