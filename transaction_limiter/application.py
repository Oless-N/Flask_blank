from flask import Flask
from healthcheck import HealthCheck
from setting import get_config
from flask_sqlalchemy import SQLAlchemy
from modules.view import health_database, blue_print


app = Flask(__name__)

app.config.update(get_config()["SERVER"])
db = SQLAlchemy(app)
health = HealthCheck(app, "/health")
app.register_blueprint(blue_print, url_prefix='/')

health.add_check(health_database)

