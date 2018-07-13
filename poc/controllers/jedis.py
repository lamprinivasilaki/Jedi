from flask import Blueprint, request
from flask.json import jsonify
from flask_restplus import Resource
from restplus import api


jedi = [
    {"name": "Qui-Gon Jinn", "id": 1},
    {"name": "Obi-Wan Kenobi", "id": 2},
    {"name": "Anakin Skywalker", "id": 3},
    {"name": "Mace Windu", "id": 4}
]

ns = api.namespace('jedi', description='Operations on Jedi')


@ns.route('/welcome')
class JediHome(Resource):
    def get(self):
        jedi_greetings = "Welcome to the Jedi Home"
        return jedi_greetings


@ns.route('/all')
class JediAll(Resource):
    def get(self):
        return jsonify({'jedi': jedi})


@ns.route('/<jedi_id>')
class JediById(Resource):
    def get(self, jedi_id):
        for j in jedi:
            if j["id"] == int(jedi_id):
                return jsonify({'jedi': j})

        return jsonify({'jedi': jedi})


@ns.route('', methods=["POST"])
class JediCreate(Resource):
    def post(self):
        count = len(jedi) + 1
        jedi_name = request.get_json()["name"]

        jedi.append({"name": jedi_name, "id": count})

        return jsonify({'jedi': jedi})


@ns.route('', methods=["PUT"])
class JediUpdate(Resource):
    def put(self):
        count = len(jedi) + 1
        jedi_name = request.get_json()["name"]
        jedi_movie = request.get_json()["movie"]

        for j in jedi:
            if j["name"] == jedi_name:
                j["movie"] = jedi_movie
                jedi[j["id"]]["movie"] = jedi_movie
                return jsonify({'jedi': j})

        jedi.append({"name": jedi_name, "id": count})

        return jsonify({'jedi': jedi})
