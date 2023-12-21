import os
from book.settings.settings import DEBUG

from django.core.wsgi import get_wsgi_application

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book.settings.production')

application = get_wsgi_application()
