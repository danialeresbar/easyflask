import os

from flask import Flask, render_template, send_from_directory
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# Blueprints imports
from app.auth.views import auth_bp
from app.bookstore.views import bookstore_bp


csrf = CSRFProtect()

# Define the database object which is imported by modules and controllers
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """
    Application-factory pattern
    :return: The flask app instance
    """

    # Define the WSGI application object
    app = Flask(__name__, instance_relative_config=True)

    # Flask app settings module
    environment = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object('app.settings.{}'.format(environment))

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from app.auth.models import User
    from app.bookstore.models import Author, Book

    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    # Sample HTTP error handling
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html')

    @app.route("/static/<path:filename>")
    def staticfiles(filename):
        return send_from_directory(app.config["STATIC_FOLDER"], filename)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(bookstore_bp)

    return app
