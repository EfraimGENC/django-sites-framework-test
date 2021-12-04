from .base import *

DEBUG = env('DEBUG')

ALLOWED_HOSTS = [
    '127.0.0.1',
    '139.59.132.237',
    'sitesf1.kavimdigital.com',
    'sitesf2.kavimdigital.com',
    'sitesf3.kavimdigital.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / env('DB'),
    }
}