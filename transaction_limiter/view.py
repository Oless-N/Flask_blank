from time import time
from datetime import datetime
from flask import Blueprint, request, jsonify


blue_print = Blueprint('blue_print', __name__)

def add_tr(client_id, ts):
    pass

def get_curent_tr():
    pass

@blue_print.route('index')
def show_page():
    ts = time()
    client_id = request.headers.get("client_id")

    res = {
        "result": "OK",
        "timestamp": datetime.fromtimestamp(ts),
        "client_id": client_id
    }
    return jsonify(res)


def health_database():
    try:
        print("--- CHECK ----")
        return True, 'It works'
    except Exception as e:
        return False, str(e)
