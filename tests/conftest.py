import configparser
import os

import pytest


@pytest.fixture
def _setting():
    app_conf = os.getenv(
        'BASE_CONFIG_FILE_PATH', '/service/tests/configs/configs.ini')

    config = configparser.ConfigParser()
    if not config.read([app_conf]):
        raise FileNotFoundError(
            'Config file not found: {}'.format(app_conf))
    return config

@pytest.fixture
def get_endpoint_url():
    return "http://0.0.0.0:5050/request"