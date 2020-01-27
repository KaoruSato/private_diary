from .settings_common import *


DEBUG = True

ALLOWED_HOSTS = []


# Logging settings
LOGGING = {
    'version': 1, # 1 fixed
    'disable_existing_loggers': False,

    # Logger settings
    'loggers': {
        # The logger used by Django
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # The logger used by the diary app
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # Handler settings
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # Formatter settings
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT =os.path.join(BASE_DIR, 'media')
