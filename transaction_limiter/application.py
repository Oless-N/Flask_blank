import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from healthcheck import HealthCheck

from setting import get_config
import view

logger = logging.getLogger("WEB_API")

def create_app():
    app = Flask(__name__)
    app.config.update(get_config()["SERVER"])
    health = HealthCheck(app, "/health")
    app.register_blueprint(view.blue_print, url_prefix='/')

    health.add_check(view.health_database)

    with app.app_context():
        db = SQLAlchemy(app)

    return app

#
# @app.errorhandler(RequestError)
# def handle_request_error(error):
#     response = jsonify(error.to_dict())
#     response.status_code = error.status_code
#     return response
