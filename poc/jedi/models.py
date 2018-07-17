from mongoengine import StringField, Document


class Jedi(Document):
    id = StringField()
    name = StringField()
    movie = StringField()