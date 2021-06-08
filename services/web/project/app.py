import os

from flask import Flask, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()

app = Flask(__name__)
environment = os.environ.get('FLASK_ENV', 'development')
app.config.from_object('project.settings.{}'.format(environment))
csrf.init_app(app)
database = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('auth/login.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('errors/404.html')


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


if __name__ == '__main__':
    app.run(debug=True)
