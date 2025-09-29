from fastapi import APIRouter, Depends, HTTPException
from app.schemas.director import *
from app.schemas.director import ReadDirector, CreateDirector
from sqlalchemy.orm import Session 
from app.models import get_db
from app.models.director import Director

router = APIRouter(prefix="/director", tags=["Director"]) #!테그는 무조건 리스트로 줄 것

# 감독 목록 추가하기
@router.post("/", response_model=ReadDirector)
def create_director(director: CreateDirector, db: Session = Depends(get_db)):
    # new_director = Director( #?<< 이렇게 안쓰는건 비효율 적이라
    # name=director.name,
    # nationality=director.nationality,
    # birth_date=director.birth_date,
    # biography=director.biography
    # )
    new_director = Director(**director.dict())  #?<< 이렇게 json파일을 딕셔너리로 바꾸고 언패킹하는 형식으로 한다고함. 결과적으로 똑같은데 코드가 짧아짐.
    db.add(new_director)
    db.commit()
    db.refresh(new_director)
    return new_director

# 감독 목록 불러오기
@router.get("/", response_model=list[ReadDirector])
def read_directors(db: Session = Depends(get_db)):
    dir_list = db.query(Director).all()
    return dir_list

# 특정 감독 불러오기
@router.get("/{director_id}", response_model=ReadDirector)
def read_director(director_id: int, db: Session = Depends(get_db)):
    # director = db.query(Director).get(director_id) #?<< 요즘에는 이렇게 안쓰고.
    director = db.get(Director, director_id)    #?<< 요렇게 쓴다고 함.
    if not director:
        raise HTTPException(status_code=404, detail="해당 감독을 찾을 수 없음")
    return director