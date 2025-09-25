from app.models import SessionLocal, Post #run.py에서 실행하니 못찾아서 app.models라고 해야함
from flask import Blueprint, request, session,render_template, redirect, url_for
from flask.views import MethodView


# 블루프린트 생성
cp_bp = Blueprint("cp", __name__, url_prefix="/cp")


class CreatePost(MethodView):
    ##################포스팅 페이지###################
    def get(self):
        return render_template("createpost.html")
    
    ##################포스팅###################
    def post(self):
        db = SessionLocal()
        data = request.get_json()
        
        # 로그인된 유저 정보 가져오기 (예시: 세션에 저장했다고 가정)
        user_id = session.get("user_id")

        if not user_id: # 세션에 아이디가 없으면 로그인 화면으로 돌아감
            return redirect(url_for("signin.sign_in"))
        
        new_post = Post(
            user_id=user_id,
            category=data["category"],
            title=data["title"],
            content=data["content"],
        )
        db.add(new_post)
        db.commit()
        db.close()
        return redirect(url_for("blog.blog"))
    

# 블루프린트 등록
cp_bp.add_url_rule("/", view_func=CreatePost.as_view("cp"))