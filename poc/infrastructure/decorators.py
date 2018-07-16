from marshmallow import Schema
from flask.json import jsonify


def dump_with_schema(schema: Schema):
    def decorator(func):
        def wrapper(*args, **kwargs) -> str:
            response = func(*args, **kwargs)

            return jsonify(response)
        return wrapper
    return decorator
