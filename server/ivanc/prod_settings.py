"""
Django settings for ivanc project.
Settings for production environment
"""

import dj_database_url
from base_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['api.ivanc.uk']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Because of warning:
# Your SECURE_CONTENT_TYPE_NOSNIFF setting is not set to True, so your pages will not be served with
# an 'x-content-type-options: nosniff' header. You should consider enabling this header to prevent
# the browser from identifying content types incorrectly.
SECURE_CONTENT_TYPE_NOSNIFF = True
# Because of warning:
# Your SECURE_BROWSER_XSS_FILTER setting is not set to True, so your pages will not be served with
# an 'x-xss-protection: 1; mode=block' header. You should consider enabling this header to activate
# the browser's XSS filtering and help prevent XSS attacks.
SECURE_BROWSER_XSS_FILTER = True
# Because of warning:
# SESSION_COOKIE_SECURE is not set to True. Using a secure-only session cookie makes it more
# difficult for network traffic sniffers to hijack user sessions.
SESSION_COOKIE_SECURE = True
# Because of warning:
# You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE_CLASSES, but you have not
# set CSRF_COOKIE_HTTPONLY to True. Using an HttpOnly CSRF cookie makes it more difficult for
# cross-site scripting attacks to steal the CSRF token.
CSRF_COOKIE_HTTPONLY = True
# You have 'django.middleware.csrf.CsrfViewMiddleware' in your MIDDLEWARE_CLASSES, but you have not
# set CSRF_COOKIE_SECURE to True. Using a secure-only CSRF cookie makes it more difficult for
# network traffic sniffers to steal the CSRF token.
CSRF_COOKIE_SECURE = True
# Because of warning:
# You have 'django.middleware.clickjacking.XFrameOptionsMiddleware' in your MIDDLEWARE_CLASSES,
# but X_FRAME_OPTIONS is not set to 'DENY'. The default is 'SAMEORIGIN', but unless there is a good
# reason for your site to serve other parts of itself in a frame, you should change it to 'DENY'.
X_FRAME_OPTIONS = 'DENY'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# Uses database config from env variable DATABASE_URL
# More info: https://github.com/kennethreitz/dj-database-url
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=500)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Amazon Web Services django-storages config
AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Configure media files using Amazon Web Services with django-storages
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Settings for https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_WHITELIST = ('ivanc.uk')
