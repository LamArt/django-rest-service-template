import os
from datetime import timedelta

from django.conf import settings

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000' # the domain for front-end app(you can add more than 1)
]

SIMPLE_JWT = { # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=500),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=100)
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
    }
}