#!/usr/bin/env python
"""Flask's command-line utility for administrative tasks."""
from flask.cli import FlaskGroup

from app import create_app
# from app.auth.models import *
# from app.bookstore.models import *


cli = FlaskGroup(create_app())


if __name__ == '__main__':
    cli()
