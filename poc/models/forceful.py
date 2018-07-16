from marshmallow import Schema, fields


class ForcefulSchema(Schema):
    id = fields.Number()
    name = fields.String()
    movie = fields.String()