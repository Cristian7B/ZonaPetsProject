from ZonaPetsBackend.base_settings import *

import os
from dotenv import load_dotenv

load_dotenv()


DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET_KEY') 