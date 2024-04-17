### 모듈 로딩
from flask import Flask, Blueprint


### 어플리케이션 팩토리 함수
def create_app():
    myapp = Flask(__name__)

    # bp 등록
    from .views import main_views

    myapp.register_blueprint(main_views.bp)

    return myapp


# ### 전역변수
# myapp = Flask(__name__)


# ### 사용자 요청 URL 처리 기능 => 라우팅(Routing)
# ### 형식 : @Flask_instance_name.route(URL문자열)
# ### 웹 서버의 첫 페이지 : http://127.0.0.1:5000/
# @myapp.route("/")
# def index_page():
#     # return "<h3><font color='green'>My Web Index Page</font></h3>"
#     return render_template("tem.html")


# ### 사용자마다 페이지 반환
# ### 사용자 페이지 URL : http://127.0.0.1:5000/<username>
# @myapp.route("/<username>")
# def username(username):
#     return f"username : {username}"


# @myapp.route("/<int:int_number>")
# def int_number(int_number):
#     return f"number : {int_number}"


# @myapp.route("/<float:float_number>")
# def float_number(float_number):
#     return f"float : {float_number}"


# @myapp.route("/<path:path_str>")
# def path_str(path_str):
#     return f"path : {path_str}"


# @myapp.route("/<uuid:uuid_str>")
# def uuid_str(uuid_str):
#     return f"uuid : {uuid_str}"


# @myapp.route("/hello/")
# def hello():
#     return "hello"


# ### 실행 제어
# if __name__ == "__main__":
#     # Flask 웹 서버 구동
#     myapp.run(debug=True)
