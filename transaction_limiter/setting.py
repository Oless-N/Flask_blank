import configparser
import os
from os.path import abspath


def get_config():
    path = abspath("configs.ini")
    app_conf = os.getenv(
        'BASE_CONFIG_FILE_PATH', '/service/configs/config.ini')

    config = configparser.ConfigParser()
    if not config.read([app_conf]):
        raise FileNotFoundError(
            'Config file not found: {}'.format(app_conf))
    return config
