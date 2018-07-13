from flask import Flask
from controllers.jedis import jediB
from controllers.siths import sithB


def create_application():
    flask_app = Flask(__name__)

    flask_app.register_blueprint(jediB, url_prefix="/jedi")
    flask_app.register_blueprint(sithB, url_prefix="/sith")

    return flask_app
