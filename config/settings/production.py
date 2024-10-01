from .base import *
from django.core.management.utils import get_random_secret_key

ALLOWED_HOSTS = ['*']


SECRET_KEY = get_random_secret_key()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
