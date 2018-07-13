from flask import Blueprint, request
from flask.json import jsonify


jedi = [
    {"name": "Qui-Gon Jinn", "id": 1},
    {"name": "Obi-Wan Kenobi", "id": 2},
    {"name": "Anakin Skywalker", "id": 3},
    {"name": "Mace Windu", "id": 4}
]

jediB = Blueprint('jedi', __name__)


@jediB.route('/welcome')
# class JediWelcome():
def get_jedi_home():
    jedi_greetings = "Welcome to the Jedi Home"
    return jedi_greetings


@jediB.route('/all')
# class Jedis:
def get_all_jedi():
    return jsonify({'jedi': jedi})


@jediB.route('/<jedi_id>')
# class Jedi:
def get_jedi(jedi_id):

    for j in jedi:
        if j["id"] == int(jedi_id):
            return jsonify({'jedi': j})

    return jsonify({'jedi': jedi})


@jediB.route('', methods=["POST"])
# class CreateJedi:
def post_jedi():

    count = len(jedi) + 1
    jedi_name = request.get_json()["name"]

    jedi.append({"name": jedi_name, "id": count})

    return jsonify({'jedi': jedi})


@jediB.route('', methods=["PUT"])
# class UpdateJedi:
def put_jedi():

    count = len(jedi) + 1
    jedi_name = request.get_json()["name"]
    jedi_movie= request.get_json()["movie"]

    for j in jedi:
        if j["name"] == jedi_name:
            j["movie"] = jedi_movie
            jedi[j["id"]]["movie"] = jedi_movie
            return jsonify({'jedi': j})

    jedi.append({"name": jedi_name, "id": count})

    return jsonify({'jedi': jedi})
