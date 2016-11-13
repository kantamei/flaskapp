#-*- coding:utf-8 -*-
from flask import render_template, flash, redirect, request, url_for
from app import app
from .forms import LoginForm, RegisterForm
from .models import User
from flask_login import login_user

from  flask_mail import Message

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    return render_template('index.html', users = users)

@app.route('/login', methods=('GET', 'POST'))
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter_by(email=loginform.email.data).first()
        if user is not None and user.password == loginform.password.data:
            login_user(user, loginform.remember.data)
            return redirect('index')
        flash('Invalid username or password.')
    return render_template('login.html', form=loginform)

@app.route('/register', methods=('GET', 'POST'))
def register():
    registerform = RegisterForm()
    if registerform.validate_on_submit():
        return '你点了注册按钮'
    return render_template('register.html', form=registerform)


