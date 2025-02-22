import os

from .base import *



SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DEBUG = False

ADMINS = [
    ('Syny', 'synek.o@seznam.cz'),
]


ALLOWED_HOSTS = ['localhost', 'filateliestafl.eu', 'www.filateliestafl.eu', ]

CSRF_TRUSTED_ORIGINS = [
    "http://www.filateliestafl.eu",
    "https://www.filateliestafl.eu",
]





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["POSTGRES_DB_NAME"],
        'USER': os.environ["POSTGRES_DB_USER"],
        'PASSWORD': os.environ["POSTGRES_DB_PASSWORD"],
        'HOST': 'db',  # This should match the service name in docker-compose.yml
        'PORT': '5432',
    }
}






# Define log directory (inside the container)
LOG_DIR = BASE_DIR / "logs"

# Ensure the directory exists
os.makedirs(LOG_DIR, exist_ok=True)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime} {levelname} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": LOG_DIR / "django_errors.log",
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

