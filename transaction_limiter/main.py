from application import logger, app, load_blueprints, print_all_routes
from setting import get_config

load_blueprints()
print_all_routes()

if __name__ == '__main__':
    logger.info('Application started', extra={'MESSAGE_ID': "Start API"})
    app.run(host=get_config()["SERVER"].get('HOST'),
            port=get_config()["SERVER"].get('PORT'),
            debug=True)
