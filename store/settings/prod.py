from .common import *
import os
import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['kubbuy-prod.onrender.com']

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.environ['MYSQL_DATABASE'],
    'HOST': 'mysql-4dyg',
    'PORT': '3306',
    'USER': os.environ['MYSQL_USER'],
    'PASSWORD': os.environ['MYSQL_PASSWORD'],
}}
#REDISCLOUD_URL = os.environ['REDISCLOUD_URL']

#CELERY_BROKER_URL = REDISCLOUD_URL


# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": REDISCLOUD_URL,
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
