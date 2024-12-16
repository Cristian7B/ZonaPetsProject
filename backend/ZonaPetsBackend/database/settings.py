from backend.ZonaPetsBackend.ZonaPetsBackend.base_settings  import *

import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET_KEY') 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'DB_NAME'),
        'USER': os.getenv('DB_USER', 'DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'DB_HOST'), 
        'PORT': os.getenv('DB_PORT', 'DB_PORT'),
    }
}
