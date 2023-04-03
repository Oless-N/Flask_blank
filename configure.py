
import logging
import pathlib

# from utils.environment import env

PATH = pathlib.Path(__file__).parent
CERTS_PATH = PATH / 'certificates'
LOGS_PATH = PATH / 'LOG'


#POSTGRES
# POSTGRES={
#     'user': 'postgres',
#     'password': '',
#     'db': 'postgres',
#     'host': 'localhost',
#     'port': 32778}
#
# # SQLAlchemy
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost:32769/flask_family_recipes_app'
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# Flask server setting

SQLITE_DB_PATH = 'sqlite:///sqlite.db'

SERVER = {
    'DEBUG': True,
    'HOST': 'localhost',
    'PORT': 5701,
    'SECRET_KEY': 'securestring',
    'JSON_AS_ASCII': False,
    'SQLALCHEMY_DATABASE_URI':SQLITE_DB_PATH,
    'SQLALCHEMY_TRACK_MODIFICATIONS': True
}


# Logstash config
LOGSTASH = {
    "HOST": 'localhost',
    "PORT": 5500,
    "VERSION": 1,
    "TCP": True,
}

# Logging setting with handler and formatting message
LOGS_PATH.mkdir(exist_ok=True)
LOGGIN_LEVEL = 'INFO',
MAX_SIZE_LOG_FILE = 10485760,
BACKUP_LOG_COUNT = 10,

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'formatter_to_file': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'formatter_std_out': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'formatter_to_logstash': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'file_handler': {
            'backupCount': BACKUP_LOG_COUNT,
            'class': 'logging.handlers.RotatingFileHandler',
            'encoding': 'utf8',
            'filename': LOGS_PATH / 'LOGS.log',
            'formatter': 'formatter_to_file',
            'level': logging.INFO,
            'maxBytes': MAX_SIZE_LOG_FILE
        },
        'error_file_handler': {
            'backupCount': BACKUP_LOG_COUNT,
            'class': 'logging.handlers.RotatingFileHandler',
            'encoding': 'utf8',
            'filename': LOGS_PATH / 'errors.log',
            'formatter': 'formatter_to_file',
            'level': logging.ERROR,
            'maxBytes': MAX_SIZE_LOG_FILE
        },
        'console': {
            'level': logging.INFO,
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_std_out'
        },
        'logstash_handler': {
            'level': logging.INFO,
            'class': 'logstash.TCPLogstashHandler' if LOGSTASH.get('TCP', True) else 'logstash.LogstashHandler',
            'host': LOGSTASH.get('HOST'),
            'port': LOGSTASH.get('PORT'),
            'version': LOGSTASH.get('VERSION'),
            # Version of logstash event schema. Default value: 0 (for backward compatibility of the library)
            'message_type': 'logstash',  # 'type' field in logstash message. Default value: 'logstash'.
            'fqdn': False,  # Fully qualified domain name. Default value: false.
            'tags': ['api_flask_blank', 'python'],  # list of tags. Default: None.
        },
    },
    'loggers': {
        'ukey': {
            'handlers': ['console', 'file_handler', 'error_file_handler', 'logstash_handler'],
            'level': LOGGIN_LEVEL,
            'propagate': True,
        }
    }
}