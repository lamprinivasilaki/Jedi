from marshmallow import Schema, fields


class JediSchema(Schema):
    id = fields.Number()
    name = fields.String()
    movie = fields.String()