from flask import Flask, Blueprint
from restplus import api
from controllers.jedis import ns as jedi_namespace
from controllers.siths import ns as sith_namespace


def create_application():
    flask_app = Flask(__name__)

    rest_api_blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(rest_api_blueprint)

    api.add_namespace(jedi_namespace)
    api.add_namespace(sith_namespace)

    flask_app.register_blueprint(rest_api_blueprint)

    return flask_app
