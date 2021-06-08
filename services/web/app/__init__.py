import os

from flask import Flask, render_template, request, send_from_directory
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from app.auth.views import auth_bp


csrf = CSRFProtect()

# Define the WSGI application object
app = Flask(__name__)

# Flask app settings module
environment = os.environ.get('FLASK_ENV', 'development')
app.config.from_object('app.settings.{}'.format(environment))

csrf.init_app(app)

# Define the database object which is imported by modules and controllers
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Sample HTTP error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html')


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


# Register blueprints
app.register_blueprint(auth_bp)
