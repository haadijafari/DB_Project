import os
from book.settings.settings import DEBUG
from django.core.asgi import get_asgi_application

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book.settings.production')

application = get_asgi_application()
