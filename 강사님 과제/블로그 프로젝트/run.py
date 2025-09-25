from flask import Flask
from app.routes.signin import signin_bp
from app.routes.signup import signup_bp
from app.routes.blog import blog_bp
from app.routes.createpost import cp_bp
from app.routes.postdt import post_bp

app = Flask(__name__, template_folder="app/templates") # app안에 templates을 넣으면 경로지정을 따라로 해줘야함.

app.secret_key = "asdlkfjonsdlkjf@askdjofk!@$#$"

app.register_blueprint(signin_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(cp_bp)
app.register_blueprint(post_bp)

if __name__=="__main__":
    app.run(debug=True)