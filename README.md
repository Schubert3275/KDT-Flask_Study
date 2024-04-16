## Web 활용

<details>
<summary>사용 교재</summary>

![](./images/Do%20it!%20점프%20투%20플라스크.png)

</details>

### DAY01

---

<details>
<summary> Flask 살펴보기 </summary>

* 설치 : conda install -c conda-forge flask
* 템플릿 엔진
  + 지정된 템플릿 양식과 특정 데이터를 합성하여 결과 HTML 문서를 출력하는 SW
* 소프트웨어 디자인 패턴
  + 소프트웨어 설계에서 공통 발생하는 문제에 대해 자주 쓰이는 설계 방법 정리한 패턴
  + 개발 효율성, 유지 보수성, 운용성 및 프로그램 최적화에 도움
* 소프트웨어 디자인 패턴 - MVC
  + 모델(model), 뷰(view), 컨트롤러(controller) 세가지 역할로 구분한 패턴
  + 모델 -> 백그라운드 로직, 데이터 조작 즉, DB 제어 담당
  + 뷰 -> 사용자가 볼 수 있는 화면, 최종적인 출력 담당
  + 컨트롤러 -> 요청 데이터 처리, 흐름 제어(전체적인 관리)
* 소프트웨어 디자인 패턴 - MVT
  + 모델(model), 뷰(view), 템플릿(template) 세가지 역할로 구분한 패턴
  + 모델 -> 백그라운드 로직, 데이터 조작 즉, DB 제어 담당
  + 뷰 -> 요청 데이터 처리, 흐름 제어(전체적인 관리)
  + 템플릿 -> 사용자가 볼 수 있는 화면, 최종적인 출력 담당

</details>
<details>
<summary> WEB 개념 및 용어 </summary>

* URI
  + 통합자원식별자, 인터넷 상에서 자원 식별하기 위한 고유한 문자열
  + 하위 개념 : URL, URN
* 127.0.0.1 또는 localhost
  + 네트워크에서 사용하는 자신의 컴퓨터 의미
  + 가상으로 인터넷망에 연결되어 있는 것처럼 할당하는 인터넷 주소
* 애플리케이션 root
  + 앱을 실행하는 디렉토리
  + 모듈이나 패키지를 읽어들이는 경로
* 라우팅(Routing)
  + 사용자가 요청한 URL에 따라 해당 URL에 맞는 페이지를 보여주는 것
* DNS(Domain Name Server)
  + 도메인 이름에 해당하는 IP 주소 반환 서버
* ISP(Internet Service Provider)
  + SKT, KT, LGU+ 등 DNS 서버의 도메인명 IP 주소 제공 사업자
* Web Server
  + 웹 브라우저 클라이언트로부터 HTTP 요청을 받아 정적인 컨텐츠(.html .jpeg .css등) 제공 SW
  + Apache server, Microsoft IIS, Nginx, Goole Web Ser, ...
* WAS : Web Application Server
  + DB 조회나 다양한 로직 처리를 요구하는 동적인 컨텐츠 제공하기 위해 만들어진 SW
  + Web Server 기능들을 구조적으로 분리하여 처리하고자 하는 목적
  + Tomcat, JBoss, Jeus, Web Sphere, ...
* WSGI(Web Server Gateway Interface)
  + 웹 서버와 웹 어플리케이션 서버 간의 통신하는 규칙이 필요
  + Web Server에서 요청한 정보를 Application에 전달하기 위해 사용하는 인터페이스

</details>

---

| 파일명          | 내용       |
| --------------- | ---------- |
| `DAY_01\MiniWeb\app.py` | flask 웹 서버 구동 |
