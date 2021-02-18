from mongoengine import Document, StringField, FloatField


class Product(Document):
    name = StringField()
    desc = StringField()
    value = FloatField()

    def serialize(self):
        return {"name": self.name, "description": self.desc, "value": self.value}
