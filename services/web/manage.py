#!/usr/bin/env python
"""Flask's command-line utility for administrative tasks."""
from flask.cli import FlaskGroup

from project import app


cli = FlaskGroup(app)


if __name__ == '__main__':
    cli()
