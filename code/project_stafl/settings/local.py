from .base import *



SECRET_KEY = 'django-insecure-(#7=l)!ra&ct9ojtjc2^qm+m0pn$(9z*c6x3m186(wh-smts(+'


DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
