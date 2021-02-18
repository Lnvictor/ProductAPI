from mongoengine import Document, StringField, FloatField


class Product(Document):
    name = StringField()
    description = StringField()
    value = FloatField()

    def serialize(self):
        return {
            "name": self.name,
            "description": self.description,
            "value": self.value
        }