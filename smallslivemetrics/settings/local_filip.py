from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smallslive-metrics',
        'USER': 'bezidejni',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'auth_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smallslive',
        'USER': 'bezidejni',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}

# CORS headers
CORS_ORIGIN_WHITELIST = (
    'localhost:8000'
)
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'OPTIONS'
)

SMALLSLIVE_SITE = 'http://localhost:8000'
