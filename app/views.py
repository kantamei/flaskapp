from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from .models import User

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    print(User.query.all())
    return render_template('index.html', users = users)

