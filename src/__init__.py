from config import Config
from flask import Flask, redirect
from pymongo import MongoClient


class StartUp:
    db = None

    @classmethod
    def create_app(cls):
        app = Flask(__name__)
        client = MongoClient(Config.MONGO_URI)
        cls.db = client[Config.DATABASE]
        app.secret_key = Config.SECRET_KEY


        from src.controlers.auth import auth_bp
        from src.controlers.user_events import dashboard_bp
        app.register_blueprint(dashboard_bp)
        app.register_blueprint(auth_bp)

        @app.route("/")
        def main():
            return redirect("/login")

        return app