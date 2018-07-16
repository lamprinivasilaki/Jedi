from flask_restplus import Resource
from restplus import api
from webargs.flaskparser import use_kwargs

from models.jedi import JediSchema
from infrastructure.decorators import dump_with_schema


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


@ns.route('')
class JediList(Resource):

    @dump_with_schema(JediSchema(dump_only=("id", "name")))
    def get(self):
        return jedi

    @use_kwargs(JediSchema(only=(["name"])))
    @dump_with_schema(JediSchema())
    def post(self, name):
        count = len(jedi) + 1
        jedi_name = name

        jedi.append({"name": jedi_name, "id": count})

        return jedi

    @use_kwargs(JediSchema(only=("name", "movie")))
    @dump_with_schema(JediSchema())
    def put(self, name, movie):
        jedi_name = name
        jedi_movie = movie

        for j in jedi:
            if j["name"] == jedi_name:
                j["movie"] = jedi_movie

                position = int(j["id"]) - 1
                jedi[position]["movie"] = jedi_movie

                return j

        return jedi


@ns.route('/<jedi_id>')
class Jedi(Resource):

    @dump_with_schema(JediSchema())
    def get(self, jedi_id):
        for j in jedi:
            if j["id"] == int(jedi_id):
                return j

        return jedi
