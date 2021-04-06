from flask import render_template, url_for, flash, redirect, request
from website import app, db
from website.forms import Login, Register
import os
import numpy as np
from website.models import User, Dataset
from flask_login import login_user, current_user, logout_user, login_required
import bcrypt
import shutil

@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already authenticated','success')
        return redirect(url_for('home'))
    form = Register()
    if form.validate_on_submit():
        hashed = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        user = User(username=form.username.data, password=hashed)
        db.session.add(user)
        db.session.commit()
        if not os.path.exists(f"website/static/uploads/{form.username.data}"):
            os.mkdir(f"website/static/uploads/{form.username.data}")
        flash(f'Created account for {form.username.data}. You may now log in.', 'success')
        return redirect(url_for('login'))

    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already authenticated','success')
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.checkpw(form.password.data.encode('utf-8'), user.password):
            login_user(user, remember=form.rememberMe.data)
            return redirect(url_for('home'))
        else:
            flash('Error Logging In', 'danger')
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    # datasets = Dataset.query.filter_by(author=current_user).all()
    # return render_template('account.html', datasets=datasets)
    return render_template('account.html')

