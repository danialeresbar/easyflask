import os
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent


class Config:
    STATIC_FOLDER = f"{os.getenv('USER_HOME', '')}/app/project/static"
    MEDIA_FOLDER = f"{os.getenv('USER_HOME', '')}/app/project/media"
