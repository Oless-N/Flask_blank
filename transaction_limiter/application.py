import logging

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from healthcheck import HealthCheck

from setting import get_config
from utilites.exceptions import RequestError

logger = logging.getLogger("WEB_API")

app = Flask(__name__)
app.config.update(get_config()["SERVER"])
db = SQLAlchemy(app)

health = HealthCheck(app, "/health")

def load_blueprints():
    from modules.webapi import view

    app.register_blueprint(view.blue_print, url_prefix='/')

    health.add_check(view.health_database)


def print_all_routes():
    print("Routes")
    SERVER = get_config()["SERVER"]
    for rule in app.url_map.iter_rules():
        print(f'http://{SERVER["HOST"]}:{SERVER["PORT"]}{rule}')


@app.errorhandler(RequestError)
def handle_request_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
