from flask import Blueprint, request
from flask.json import jsonify
from restplus import api
from flask_restplus import Resource
from marshmallow import Schema, fields


def dump_with_schema(schema: Schema):
    def decorator(func):
        def wrapper(*args, **kwargs) -> str:
            response = func(*args, **kwargs)

            return jsonify(response)
        return wrapper
    return decorator


class SithSchema(Schema):
    id = fields.Number()
    name = fields.String()
    movie = fields.String()


sith_lords = [
    {"id": 1, "name": "Darth Vader", "movie": "A New Hope"},
    {"id": 2, "name": "Darth Bane", "movie": "The Phantom Menace"},
    {"id": 3, "name": "Darth Sidious", "movie": "A New Hope"},
]

ns = api.namespace('sith', description='Operations on Sith Lords')


@ns.route('')
class Sith(Resource):

    @dump_with_schema(SithSchema())
    def get(self):
        sith_id = request.args.get("id")
        movie = request.args.get("movie")

        for sith in sith_lords:
            if sith["id"] == int(sith_id) and sith["movie"] == movie:
                return sith

        return sith_lords

