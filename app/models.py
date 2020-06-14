
from datetime import datetime
from app import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary)

    def to_dict(self):
        data = {'id': self.id,'image':self.image}
        return data

    def from_dict(self, data, new_user=False):
        for field in ['image']:
            if field in data:
                setattr(self, field, data[field])

