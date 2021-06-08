from .common import *
from .partials.utils import get_secret


DEBUG = False

# Secret key for signing cookies
SECRET_KEY = get_secret('SECRET_KEY')
