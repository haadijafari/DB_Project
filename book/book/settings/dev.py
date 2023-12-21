from .settings import *

ALLOWED_HOSTS = [
    '127.0.0.1',
]

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static_cdn'
MEDIA_ROOT = BASE_DIR / 'media_cdn'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "media",
]


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
