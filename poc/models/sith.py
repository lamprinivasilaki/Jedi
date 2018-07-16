from marshmallow import Schema, fields


class SithSchema(Schema):
    id = fields.Number()
    name = fields.String()
    movie = fields.String()