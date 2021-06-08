import os
from pathlib import Path


# Environment
ENVIRONMENT = os.environ.get('FLASK_ENV', 'development')
IS_PRODUCTION = ENVIRONMENT == "production"

# Define the application directory
# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, Images)
STATIC_FOLDER = f"{os.getenv('USER_HOME', '')}/app/project/static"
MEDIA_FOLDER = f"{os.getenv('USER_HOME', '')}/app/project/media"
