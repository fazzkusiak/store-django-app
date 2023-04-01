from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nk4%6-f4#%*49hrzaue_!@5u@2r8f!-f3cld5s=3d8$y0-=5ck'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CELERY_BROKER_URL = 'redis://localhost:6379/1'


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
