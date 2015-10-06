import dj_database_url
from .base import *

def env_var(key, default=None):
    """Retrieves env vars and makes Python boolean replacements"""
    val = os.environ.get(key, default)
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val

SECRET_KEY = os.environ.get("SECRET_KEY", "herokudefault")


DATABASES['default'] = dj_database_url.config()
DATABASES['auth_db'] = dj_database_url.config('AUTH_DB_URL')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# CORS headers
CORS_ORIGIN_WHITELIST = (
    'beta.smallslive.com',
    'ssltest.smallslive.com',
    'smallslive.com',
    'herokuapp.com'
)
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'OPTIONS'
)
