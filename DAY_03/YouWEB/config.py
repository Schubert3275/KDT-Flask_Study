import os

BASE_DIR = os.path.dirname(__file__)
DB_MANE_SQLITE = "app.db"

## 다양한 DBMS URI
DB_SQLITE_URI = f"sqlite:///{os.path.join(BASE_DIR, DB_MANE_SQLITE)}"
DB_MYSQL_URI = "mysql+pymysql://root:1234@localhost:3306/testdb"
# DB_MARIA_URI = 'mariadb+mariadb://root:1234@localhost:3306/testdb'
# DB_POST_URI = 'postgresql+pg8000://scott:tiger@localhost/test'

## 사용할 DBMS 설정/ SQLALCHEMY_시작 변수명 고정
SQLALCHEMY_DATABASE_URI = DB_MYSQL_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
