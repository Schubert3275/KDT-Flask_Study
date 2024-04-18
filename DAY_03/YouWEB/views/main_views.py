## 모듈 로딩 --------------------------------------------------------------------------------
from flask import Blueprint, render_template
from ..models import Question

## BP 인스턴스 생성 -------------------------------------------------------------------------
bp = Blueprint("main", __name__, template_folder="temlpates", url_prefix="/")


## 라우팅 함수들 ----------------------------------------------------------------------------
@bp.route("/")
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template("q_list.html", question_list=question_list)
    # return (
    #     f"<h3>HI ~^^ </h3> {question_list.first().id} {question_list.first().subject}"
    # )
