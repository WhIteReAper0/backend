from flask import Blueprint, render_template, request, redirect, url_for

from flask_login import login_user, logout_user, current_user

from database.models.auth import User
from database.engine import db 

profile_bp = Blueprint('profile', __name__, template_folder='templates')


@profile_bp.route('/profile', methods=['GET', 'post'])
def profile():
    return render_template('profile.html')