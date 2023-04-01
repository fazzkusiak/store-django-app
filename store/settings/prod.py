from .common import *
import os
import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['kubbuy-prod.fly.dev']

DATABASES = {
    'default': dj_database_url.config()
}
