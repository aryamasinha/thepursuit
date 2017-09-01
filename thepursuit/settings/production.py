import os

from thepursuit.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','35.154.85.209','thepursuit.ingeniushack.com','tiusrupeht.ingeniushack.com']

#ALLOWED_HOSTS += [os.environ['DJANGO_HOST_NAME']]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/home/ingenius/oth/thepursuit_db.cnf',
        },
    }
}


STATIC_ROOT = os.environ.get('STATIC_ROOT', None)
