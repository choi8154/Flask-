from app.models import SessionLocal, Post #run.py에서 실행하니 못찾아서 app.models라고 해야함
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask.views import MethodView


# 블루프린트 생성
blog_bp = Blueprint("blog", __name__, url_prefix="/blog")


class Blog(MethodView):
    ##################블로그 메인페이지###################
    def get(self):
        db = SessionLocal()
        posts = db.query(Post).all()
        db.close()
        return render_template("blog.html", posts=posts)
    
    ##################블로그 검색기능###################





# 블루프린트 등록
blog_bp.add_url_rule("/", view_func=Blog.as_view("blog"))