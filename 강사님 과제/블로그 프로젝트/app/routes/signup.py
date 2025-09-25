from app.models import SessionLocal, User #run.py에서 실행하니 못찾아서 app.models라고 해야함
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask.views import MethodView


# 블루프린트 생성
signup_bp = Blueprint("signup", __name__, url_prefix="/signup")

#! @user_bp.route('/') << 붙이는 방식은 안쓴다고함.
class SignUp(MethodView):
    ##################회원가입 페이지 구현###################
    def get(self):
        return render_template("signup.html")

    ####################유저 데이터 추가####################
    def post(self):
        data = request.get_json()
        db = SessionLocal()

        # 이미 등록한 유저 확인
        user = db.query(User).filter(User.login_id == data["login_id"]).first()
        if user:
            db.close()
            return jsonify({"error": "이미 등록한 유저입니다."}), 403
        
        # 새로운 유저 추가
        new_user = User(
            login_id = data["login_id"],
            password = data["password"],
            email = data["email"],
            name = data["name"],
            phone = data["phone"]
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return redirect(url_for("signin.sign_in"))

signup_bp.add_url_rule("/", view_func=SignUp.as_view("signup")) #! 이방식으로 사용