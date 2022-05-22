from curses import flash
from flask import Blueprint, render_template, redirect, url_for, request, flash

from Website import views
from . import DB_NAME, db
from .models import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST']) # allows get and post w/ out error
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("login.html")


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
    
        email_exists = User.query.filer_by(email=email).first() # looks to see if this is the only email in db
        username_exists =  User.query.filer_by(username=username).first()
        if email_exists:
            flash('Email is already in use.', category='error') # flashes this message to user
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(username) < 4:
            flash('Username is too short.', category='error')
        elif len(password1) < 6:
            flash('Password is too short.', category='error')
        elif len(email) < 4:                                    # ADD IN CODE TO CHECK FOR VAILD EMAILS LATER
            flash('Email is invalid.', category='error')
        else:
            new_user = User(email=email, username=username, password=password1)
            db.session.ass(new_user)
            db.session.commit()
            flash('User Created!')
            return redirect(url_for('views.home'))
            
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))