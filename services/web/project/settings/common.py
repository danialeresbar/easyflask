import os
from pathlib import Path


# Environment variable
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')
IS_PRODUCTION = ENVIRONMENT == "production"


# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_DIR = Path(__file__).resolve().parent.parent


# Static files (CSS, JavaScript, Images)
STATIC_FOLDER = f"{os.getenv('USER_HOME', '')}/app/project/static"
MEDIA_FOLDER = f"{os.getenv('USER_HOME', '')}/app/project/media"
