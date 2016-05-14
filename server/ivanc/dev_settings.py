"""
Django settings for ivanc project.
Settings for development environment
"""

from base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's0snuahj%bar3xj6g08(mr^xt&kmb()tt7jj29id8vn22a+544'

ALLOWED_HOSTS = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files for images uploaded to the API
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# Settings for https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_WHITELIST = ('localhost:3000', '127.0.0.1:3000')
