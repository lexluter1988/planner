from flask import Flask
from flask_babel import Babel
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


bootstrap = Bootstrap()
babel = Babel()
login = LoginManager()


def create_app():
    app = Flask(__name__)
    login.init_app(app)
    bootstrap.init_app(app)
    babel.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

