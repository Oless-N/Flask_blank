from application import logger, create_app
from setting import get_config


if __name__ == '__main__':
    logger.info('Application started', extra={'MESSAGE_ID': "Start API"})
    app = create_app()
    print("Routes")
    for rule in app.url_map.iter_rules():
        print(f'http://{get_config()["SERVER"].get("HOST")}:{get_config()["SERVER"].get("PORT")}{rule}')

    app.run(host=get_config()["SERVER"].get('HOST'),
            port=get_config()["SERVER"].get('PORT'),
            debug=True)
