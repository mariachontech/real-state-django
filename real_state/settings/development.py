from .base import *


EMAIL_BACKEND = "django.core.email.backends.smtp.EmailBackend"

EMAIL_HOST = env("EMAIL_HOST")
EMAIL_USE_TLS = True
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "info@real-estate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Real Estate"

# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres. mariachonjunco@gmail.com

DATABASES = {
    'default': {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
        "OPTIONS": {'sslmode': 'require'},
    }
}
