from app.models import SessionLocal, Post #run.py에서 실행하니 못찾아서 app.models라고 해야함
from flask import session ,Blueprint, request, jsonify, render_template, redirect, url_for
from flask.views import MethodView


# 블루프린트 생성
post_bp = Blueprint("post", __name__, url_prefix="/post")


class PostDetail(MethodView):

    ##################포스트 내용 페이지 구현###################
    def get(self, post_id):
        user_id = session.get("user_id")  # 세션에서 사용자 조회
        if not user_id: # 사용자가 포스트 아이디랑 다를시
            return redirect(url_for("signin.sign_in"))
        
        db = SessionLocal()
        post = db.query(Post).filter(Post.id == post_id).first()
        db.close()

        if not post:
            return "게시글을 찾을 수 없습니다.", 404
        
        return render_template("post.html", post=post)
    
    ##################포스트 수정###################
    def put(self, post_id):
        db = SessionLocal()
        
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            db.close()
            return jsonify({"error": "게시글을 찾을 수 없습니다."}), 404

        user_id = session.get("user_id")  # 세션에서 사용자 조회
        if not user_id or post.user_id != user_id: # 사용자가 포스트 아이디랑 다를시
            db.close() 
            return jsonify({"error": "수정 권한이 없습니다."}), 403

        data = request.get_json(silent=True) or {}
        
        if "title" in data:
            post.title = data["title"]
        if "category" in data:
            post.category = data["category"]
        if "content" in data:
            post.content = data["content"]

        db.commit()
        db.refresh(post)
        db.close()
        return jsonify({"message": "수정 완료", "post_id": post_id})
    
    ##################포스트 삭제###################
    def delete(self, post_id):
        db = SessionLocal()
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            db.close()
            return jsonify({"error": "게시글을 찾을 수 없습니다."}), 404

        user_id = session.get("user_id")
        if not user_id or post.user_id != user_id:
            db.close()
            return jsonify({"error": "삭제 권한이 없습니다."}), 403

        db.delete(post)
        db.commit()
        db.close()
        return jsonify({"message": "삭제 완료", "post_id": post_id})

# 블루프린트 등록
post_bp.add_url_rule("/<int:post_id>", view_func=PostDetail.as_view("detail"))