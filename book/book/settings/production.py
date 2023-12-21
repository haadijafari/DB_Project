from .settings import *

ALLOWED_HOSTS = [
    # 'example.com',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'haadija1_haadijafari',
        'USER': 'haadija1_haadija1',
        'PASSWORD': os.environ['SQL_PASS'],
        'HOST':'localhost',
        'PORT':'3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
