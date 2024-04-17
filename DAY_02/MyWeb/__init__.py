### Application Factory 기반의 Flask Server 구동

## 모듈 로딩
from flask import Flask, render_template, url_for


### Application Factory 기반의 함수 정의
### 함수명 : create_app 변경 불가
### 반환값 : Flask Server 인스턴스
def create_app():
    ## Flask Server 인스턴스 생성
    app = Flask(__name__)

    ## Blueprint 인스턴스 등록 : 서브 카테고리의 페이지 라우팅 기능
    from flask import Blueprint
    from .views import data_view

    app.register_blueprint(data_view.data_BP)

    ## Flask Server 인스턴스 반환
    return app
