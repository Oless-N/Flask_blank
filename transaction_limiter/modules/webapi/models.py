from application import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ts = db.Column(db.String, unique=True, nullable=False)

