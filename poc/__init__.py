from flask import Flask, Blueprint
from mongoengine import *
from restapi.restplus import api
from restapi.jedi.controllers import ns as jedi_namespace
from restapi.sith.controllers import ns as sith_namespace


connect('jedi')

def create_application():
    flask_app = Flask(__name__)

    rest_api_blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(rest_api_blueprint)

    api.add_namespace(jedi_namespace)
    api.add_namespace(sith_namespace)

    flask_app.register_blueprint(rest_api_blueprint)

    return flask_app
