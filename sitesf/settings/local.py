from .base import *


ALLOWED_HOSTS = []
DEBUG = True
SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'local_db.sqlite3',
    }
}