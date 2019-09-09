import logging

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from healthcheck import HealthCheck

logger = logging.getLogger("WEB_API")

from transaction_limiter.utilites.exceptions import RequestError
from transaction_limiter.configure import SERVER

app = Flask(__name__)
app.config.update(SERVER)

health = HealthCheck(app, "/health")

db = SQLAlchemy(app)


def load_blueprints():
    from transaction_limiter.modules.webapi import view

    app.register_blueprint(view.blue_print, url_prefix='/')

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
