import ast
import urlparse
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

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

DATABASES['default'] = dj_database_url.config()
DATABASES['default']['CONN_MAX_AGE'] = 120
DATABASES['auth_db'] = dj_database_url.config('AUTH_DB_URL')
DATABASES['auth_db']['CONN_MAX_AGE'] = 120

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = [
    '.smallslive.com',
    '.smallslive.com.',
]

ALLOWED_HOSTS = ast.literal_eval(os.environ.get('ALLOWED_HOSTS', '[]')) or ALLOWED_HOSTS

SMALLSLIVE_SITE = os.environ.get('SMALLSLIVE_SITE', 'https://www.smallslive.com')


# CORS headers
CORS_ORIGIN_WHITELIST = (
    'www.smallslive.com',
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

# Add this so staging can be configured without limitations.
CORS_ORIGIN_ALLOW_ALL = ast.literal_eval(os.environ.get('CORS_ORIGIN_ALLOW_ALL', 'False'))

# Cache
redis_url = urlparse.urlparse(get_env_variable('REDIS_URL'))
CACHEOPS_REDIS = {
    'host': redis_url.hostname,
    'port': redis_url.port,
    'db': 1,
    'password': redis_url.password,
    'socket_timeout': 5,   # connection timeout in seconds, optional
}

CACHEOPS = {
    # Automatically cache any User.objects.get() calls for 15 minutes
    # This includes request.user or post.author access,
    # where Post.author is a foreign key to auth.User
    'auth.user': {'ops': 'get', 'timeout': 60*15},

    # Automatically cache all gets and queryset fetches
    # to other django.contrib.auth models for an hour
    'auth.*': {'ops': ('fetch', 'get'), 'timeout': 60*60},

    # Cache gets, fetches, counts and exists to Permission
    # 'all' is just an alias for ('get', 'fetch', 'count', 'exists')
    'auth.permission': {'ops': 'all', 'timeout': 60*60},

    'metrics.*': {'ops': 'all', 'timeout': 5*60},
    'metrics_users.*': {'ops': 'all', 'timeout': 5*60},

    # And since ops is empty by default you can rewrite last line as:
    '*.*': {'timeout': 60*60},
}
CACHEOPS_LRU = True
CACHEOPS_DEGRADE_ON_FAILURE = True
