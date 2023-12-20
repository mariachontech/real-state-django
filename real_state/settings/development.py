from .base import *


# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.

DATABASES = {
    'default': {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
        'OPTIONS': {'sslmode': 'require'},
    }
}
