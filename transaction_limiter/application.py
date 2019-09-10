import logging

from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from healthcheck import HealthCheck

import view

logger = logging.getLogger("WEB_API")

def create_app(conf):
    app = Flask(__name__)
    app.config.update(conf["SERVER"])
    health = HealthCheck(app, "/health")
    app.register_blueprint(view.blue_print, url_prefix='/')

    health.add_check(view.health_database)

    with app.app_context():
        g.db = SQLAlchemy(app)

    return app
