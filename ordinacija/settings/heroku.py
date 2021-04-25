"""
Production Settings for Heroku
"""

import environ

# If using in your own project, update the project namespace below
from ordinacija.settings.base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# False if not in os.environ
DEBUG = True

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Parse database connection url strings like psql://user:pass@127.0.0.1:8458/db
DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}

EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
