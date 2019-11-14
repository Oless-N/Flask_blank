from datetime import datetime
from time import time

from flask import Blueprint, request, jsonify


blue_print = Blueprint("blue_print", __name__)


@blue_print.route("request")
def show_page():
    from modules.models import get_all_limiter, create_limiter

    r = None
    ts = time()
    client_id = request.headers.get("client_id")
    try:
        create_limiter(period=10, amount=1)
        r = get_all_limiter()
    except Exception as e:
        print("ERROR************", e)
    res = {
        "result": str(r),
        "timestamp": datetime.fromtimestamp(ts),
        "client_id": client_id,
    }
    return jsonify(res)


def health_database():
    try:
        return True, "It works"
    except Exception as e:
        return False, str(e)
