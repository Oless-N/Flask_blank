from transaction_limiter.application import logger, app, load_blueprints, print_all_routes

from transaction_limiter.configure import SERVER

load_blueprints()
print_all_routes()

if __name__ == '__main__':
    logger.info('Application started', extra={'MESSAGE_ID': "Start API"})
    app.run(host=SERVER.get('HOST'), port=SERVER.get('PORT'))
