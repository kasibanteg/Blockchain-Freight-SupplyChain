
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '********',           # your database name
        'USER': '**********',         # your database user
        'PASSWORD': '**********', # your database password
        'HOST': 'localhost',      # or your db host/IP
        'PORT': '5433',           # default PostgreSQL port
    }
}



