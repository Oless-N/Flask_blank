from flask import Blueprint, send_from_directory


blue_print = Blueprint('blue_print', __name__)


@blue_print.route('index')
def show_page():
    return "ok"


def health_database():
    try:
        print("--- CHECK ----")
        # db.session.query("1").from_statement("SELECT 1").all()
        return True, 'It works'
    except Exception as e:
        return False, str(e)
