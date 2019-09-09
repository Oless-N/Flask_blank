import configparser
import os


def get_config():
    app_conf = os.getenv(
        'BASE_CONFIG_FILE_PATH', '/service/configs/config.ini')

    config = configparser.ConfigParser()
    if not config.read([app_conf]):
        raise FileNotFoundError(
            'Config file not found: {}'.format(app_conf))
    return config
