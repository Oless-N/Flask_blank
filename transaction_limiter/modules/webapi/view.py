from flask import Blueprint, send_from_directory

from application import db
from modules.webapi.models import Transaction

blue_print = Blueprint('blue_print', __name__)


@blue_print.route('index')
def show_page():
    db.session.add(Transaction(name="Flask", email="example@example.com"))
    db.session.commit()

    users = Transaction.query.all()
    return "ok2"


def health_database():
    try:
        print("--- CHECK ----")
        db.session.query("1").from_statement("SELECT 1").all()
        return True, 'It works'
    except Exception as e:
        return False, str(e)
