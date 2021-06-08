#!/usr/bin/env python
"""Flask's command-line utility for administrative tasks."""
from flask.cli import FlaskGroup

from app import app, db


cli = FlaskGroup(app)


@cli.command('create_database')
def create_database():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
