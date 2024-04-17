## --------------------------------------------------------------------------------------------
## 역할 : 데이터 저장 및 출력관련 웹페이지 라우팅 처리
## URL : /input
##       /input/save
##       /input/delete
##       /input/update
## --------------------------------------------------------------------------------------------
## 모듈 로딩
from flask import Blueprint, request, render_template, url_for
import os, datetime

## BP 인스턴스 생성
data_BP = Blueprint("data", __name__, template_folder="templates", url_prefix="/input/")


## 라우팅 함수들
@data_BP.route("/")
## http://127.0.0.1:5000/input/
def input_data():
    return render_template("input_data.html")


@data_BP.route("save", methods=["GET", "POST"])
def save_data():
    if request.method == "GET":
        req_dict = request.args.to_dict()
    else:
        req_dict = request.form.to_dict()
    value = req_dict.get("value")
    msg = req_dict.get("msg")
    file = request.files["upload_file"]
    extension = "." + file.filename.rsplit(".", 1)[1]
    img_file = datetime.datetime.now().strftime("%y%m%d_%H%M%S") + extension
    # save_path = os.path.join(os.path.dirname(__file__), filename)
    save_path = f"MyWeb/static/img/{img_file}"
    file.save(save_path)
    upload_file = url_for("static", filename=f"img/{img_file}")
    print(upload_file)
    return render_template(
        "save_data.html", value=value, msg=msg, upload_file=upload_file
    )


## GET 방식으로 데이터 저장
## 사용자의 요청 즉, request 객체에 데이터 저장되어 있음
# @data_BP.route("save_get", methods=["GET"])
# ## http://127.0.0.1:5000/input/save_get
# def save_get_data():
#     # 요청 데이터 추출
#     req_dict = request.args.to_dict()
#     # value = request.args["value"]
#     # msg = request.args["msg"]
#     return render_template("save_data.html", **req_dict)


# @data_BP.route("save_post", methods=["POST"])
# ## http://127.0.0.1:5000/input/save_post
# def save_post_data():
#     req_dict = request.form.to_dict()
#     method = request.method
#     header = request.headers

#     return f"SAVE POST DATA<br><br>METHOD : {method}<br><br>HEADER : {header}<br><br>DATA : {req_dict}"
#     # value = request.form["value"]
#     # msg = request.form["msg"]
#     return render_template("save_data.html", **req_dict)
