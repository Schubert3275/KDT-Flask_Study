## 모듈 로딩 --------------------------------------------------------------------------------
from flask import Blueprint, render_template, request, redirect
from ..models import Question
from YouWEB import db

## BP 인스턴스 생성 -------------------------------------------------------------------------
bp = Blueprint("main", __name__, template_folder="temlpates", url_prefix="/")


## 라우팅 함수들 ----------------------------------------------------------------------------
@bp.route("/")
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template("question/q_list.html", question_list=question_list)


@bp.route("/question/create")
def create_question():
    return render_template("question/q_create.html")


@bp.route("/question/input_data", methods=["POST"])
def input_data():
    if request.method == "POST":
        subject = request.form["Tilte"]
        content = request.form["Content"]
        if subject and content:
            q = Question(subject=subject, content=content)
            db.session.add(q)
            db.session.commit()
    return redirect("/")
