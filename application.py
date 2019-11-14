from flask import Flask, jsonify
from healthcheck import HealthCheck
from flask_sqlalchemy import SQLAlchemy
import logging

logger = logging.getLogger("WEB_API")

from utilites.exceptions import RequestError
from configure import SERVER

app = Flask(__name__)
app.config.update(SERVER)

health = HealthCheck(app, "/health")

db = SQLAlchemy(app)


def load_blueprints():
    from modules.webapi import view

    app.register_blueprint(view.blue_print, url_prefix="/")

    health.add_check(view.health_database)


def print_all_routes():
    print("Routes")
    for rule in app.url_map.iter_rules():
        print(f'http://{SERVER["HOST"]}:{SERVER["PORT"]}{rule}')


@app.errorhandler(RequestError)
def handle_request_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
