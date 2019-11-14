from time import time

from application import db


class Limiter(db.Model):
    __tablename__ = "limiters"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    period = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    timestamp = db.Column(db.Integer)

    def __init__(self, period, amount):
        self.period = period
        self.amount = amount
        self.timestamp = time()

    def __repr__(self):
        return "<period {}>".format(self.period)


def create_limiter(period, amount):
    db.session.add(Limiter(period, amount))
    db.session.commit()


def get_limiter(period_, amount_):
    return (
        db.session.query(Limiter)
        .filter(Limiter.period.in_(period_))
        .filter(Limiter.amount.in_(amount_))
        .all()
    )


def get_all_limiter():
    return Limiter.query.all()
