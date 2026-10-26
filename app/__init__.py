

from flask import Flask, redirect, url_for

from .extensions import appbuilder, db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)

    with app.app_context():
        appbuilder.init_app(app, db.session)

    @app.route("/")
    def index():
        return redirect(url_for("AppBuilder.index"))

    return app


app = create_app()
