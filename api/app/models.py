from datetime import datetime

from .database import db

class Document(db.Model):
    doc_id = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    text = db.Column(db.Text(), nullable=False, default="")

    def __repr__(self):
        return "<doc_id: {}>: {}".format(self.doc_id, self.title)
