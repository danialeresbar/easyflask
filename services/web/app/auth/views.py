from flask import Blueprint, flash, g, redirect, request, render_template, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login/', methods=["GET", "POST"])
def login():
    form = ''
    if request.method == 'POST':
        pass
    return render_template('auth/login.html', form=form)
