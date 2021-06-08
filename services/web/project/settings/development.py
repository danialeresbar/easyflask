from .common import *


DEBUG = True
SECRET_KEY = "flaskn4%(+ftkg6-r3jl585^542-4&i(f8n*iw(p__v^o8xc^m@2qlckey"

# Database
database_settings = {
    'NAME': 'easyflask',
    'USER': 'flaskuser',
    'PASSWORD': 'mariadb',
    'HOST': 'database',
    'PORT': '3306'
}
SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}:{}/{}".format(
    database_settings.get('USER'),
    database_settings.get('PASSWORD'),
    database_settings.get('HOST'),
    database_settings.get('PORT'),
    database_settings.get('NAME')
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
