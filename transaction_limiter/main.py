import logging
import os
from application import app
from setting import get_config
from utilites.create_db import create_connection

logger = logging.getLogger("WEB_API")

if __name__ == '__main__':
    logger.info('DataBase is create ', extra={'MESSAGE_ID': "DB Created"})
    curent_path = os.path.dirname(os.path.abspath(__file__))
    create_connection(curent_path.join("sqlite.db"))

    logger.info('Application started', extra={'MESSAGE_ID': "Start API"})
    print("Routes")
    for rule in app.url_map.iter_rules():
        print(f'http://{get_config()["SERVER"].get("HOST")}:{get_config()["SERVER"].get("PORT")}{rule}')

    app.run(host=get_config()["SERVER"].get('HOST'),
            port=get_config()["SERVER"].get('PORT'),
            debug=True)

