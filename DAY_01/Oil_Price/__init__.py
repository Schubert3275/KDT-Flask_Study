from flask import Flask


def create_app():
    app = Flask(__name__)

    from .views import main_view

    app.register_blueprint(main_view.bp)

    return app
