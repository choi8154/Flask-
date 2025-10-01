from fastapi import FastAPI, APIRouter, Request, Depends, HTTPException, Form, Header, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from datetime import datetime, timedelta
import secrets, jwt, uvicorn
from typing import List, Dict, Optional

# ----------------- "DB"  -----------------
db: List[Dict] = [{"id": "admin", "password": "pw"}]
# -----------------------------------------

templates = Jinja2Templates(directory="templates")

app = FastAPI()
router = APIRouter(prefix="/homepage")


#JWT 설정
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_EXPIRE_MINUTES = 60


# 토큰 생성
def create_jwt_token(sub: str, expires_minutes: int = ACCESS_EXPIRE_MINUTES) -> str:
    now = datetime.utcnow()
    expire = now + timedelta(minutes=expires_minutes)
    payload = {
        "sub": str(sub),
        "iat": int(now.timestamp()),
        "exp": int(expire.timestamp()),
        "type": "access"
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


# 토큰 검증
def verify_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


# 의존성 함수
def get_current_user(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Missing or invalid Authorization header")
    token = authorization.split(" ", 1)[1]
    payload = verify_jwt_token(token)
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
    user = next((u for u in db if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user


# 라우터
@router.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})


@router.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request, "error": None})


# 회원가입 처리
@router.post("/signup")
def signup(username: str = Form(...), password: str = Form(...)):
    if any(u["id"] == username for u in db):
        return JSONResponse({"detail": "id already exist"}, status_code=400)
    db.append({"id": username, "password": password})
    return RedirectResponse(url="/homepage/", status_code=303)


# 토큰 발급
@router.post("/token")
def token_endpoint(username: str = Form(...), password: str = Form(...)):
    user = next((u for u in db if u["id"] == username and u["password"] == password), None)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_jwt_token(sub=user["id"])
    return {"access_token": access_token, "token_type": "bearer", "expires_in": ACCESS_EXPIRE_MINUTES * 60}


#  토큰이 있어야 접근 가능한 페이지
@router.get("/me")
def me(current_user = Depends(get_current_user)):
    return {"id": current_user["id"], "msg": "You are authenticated"}


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)