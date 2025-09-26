from app.models import SessionLocal, User #run.py에서 실행하니 못찾아서 app.models라고 해야함
from flask import Blueprint, session, request, jsonify, render_template, redirect, url_for
from flask.views import MethodView


# 블루프린트 생성
signin_bp = Blueprint("signin", __name__, url_prefix="/signin")


class SignIn(MethodView):
    ##################로그인 페이지 구현###################
    def get(self):
        return render_template("signin.html")
    
    #######################로그인#######################
    def post(self): #세션 로그인은 post가 더 안전하다고함.
        data = request.get_json()
        db = SessionLocal()

        user = db.query(User).filter(User.login_id == data["login_id"]).first()

        if not user:
            db.close()
            return jsonify({"error":"존재하지 않는 아이디 입니다."}), 404
        
        if user.password != data["password"]:
            db.close()
            return jsonify({"error":"비밀번호가 올바르지 않습니다."}), 401
            
        
        # 로그인 성공시 세션에 저장
        session["user_id"] = user.id
        session["user_name"] = user.name  

        
        db.close()

        return redirect(url_for("blog.blog"))

@signin_bp.route("/logout", methods=["GET"]) 
def logout():
    session.clear() # 로그아웃 시 세션 클리어
    return redirect(url_for("signin.sign_in"))

signin_bp.add_url_rule("/", view_func=SignIn.as_view("sign_in"))