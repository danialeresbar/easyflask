from flask import Blueprint, flash, g, redirect, request, render_template, session, url_for

bookstore_bp = Blueprint('bookstore', __name__, url_prefix='/bookstore')


@bookstore_bp.route("/", methods=["GET", "POST"])
def home():
    return render_template('home.html')
