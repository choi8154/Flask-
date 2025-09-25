from app.models import SessionLocal, Post #run.py에서 실행하니 못찾아서 app.models라고 해야함
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from flask.views import MethodView


# 블루프린트 생성
post_bp = Blueprint("post", __name__, url_prefix="/post")


class PostDetail(MethodView):
    def get(self, post_id):
        db = SessionLocal()
        post = db.query(Post).filter(Post.id == post_id).first()
        db.close()

        if not post:
            return "게시글을 찾을 수 없습니다.", 404
        
        return render_template("post.html", post=post)
    

# 블루프린트 등록
post_bp.add_url_rule("/<int:post_id>", view_funce=PostDetail.as_view("detail"))