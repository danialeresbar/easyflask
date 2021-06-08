import os

from flask import Flask, render_template, request, send_from_directory
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()

# Define the WSGI application object
app = Flask(__name__)

# Flask app settings module
environment = os.environ.get('FLASK_ENV', 'development')
app.config.from_object('project.settings.{}'.format(environment))

csrf.init_app(app)

# Define the database object which is imported by modules and controllers
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import a module/component using its blueprint handler variable (auth)
from .auth.controllers import


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('auth/login.html')

# Sample HTTP error handling
@app.errorhandler(404)
def page_not_found():
    return render_template('errors/404.html')


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


if __name__ == '__main__':
    app.run(debug=True)
