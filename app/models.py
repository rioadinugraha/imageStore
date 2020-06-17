
from datetime import datetime
from app import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(1000))
    image_filename = db.Column(db.String(1000))

    def to_dict(self):
        data = {'id': self.id,'image_url':self.image_url,'image_filename':self.image_filename}
        return data

    def from_dict(self, data):
        for field in ['image_url','image_filename']:
            if field in data:
                setattr(self, field, data[field])

