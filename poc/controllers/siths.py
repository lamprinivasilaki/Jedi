from flask import Blueprint, request
from flask.json import jsonify


sith_lords = [
    {"id": 1, "name": "Darth Vader", "movie": "A New Hope"},
    {"id": 2, "name": "Darth Bane", "movie": "The Phantom Menace"},
    {"id": 3, "name": "Darth Sidious", "movie": "A New Hope"},
]

sithB = Blueprint('sith', __name__)


@sithB.route('')
def get_sith():
    sith_id = request.args.get("id")
    movie = request.args.get("movie")

    for sith in sith_lords:
        if sith["id"] == int(sith_id) and sith["movie"] == movie:
            return jsonify({'sith': sith})

    return jsonify({'siths': sith_lords})

