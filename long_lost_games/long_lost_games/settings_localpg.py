from .settings import *

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'lostgames_localdb',
        'USER': 'lg_user',
        'PASSWORD': 'akatski2',
        'HOST': '',
        'PORT': ''
    }
}
