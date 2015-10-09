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

# Cache
redis_url = urlparse.urlparse(get_env_variable('REDIS_URL'))
CACHEOPS_REDIS = {
    'host': redis_url.hostname ,
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
