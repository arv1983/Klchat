from flask import Flask
from flask_jwt_extended import JWTManager
from environs import Env

from app.configs import database, migrate
from app import views

env = Env()
env.read_env()
jwt = JWTManager()

def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = env("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["JWT_SECRET_KEY"] = env("JWT_SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

    database.init_app(app)
    migrate.init_app(app)

    views.init_app(app)
    jwt.init_app(app)

    return app
