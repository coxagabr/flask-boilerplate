from flask import render_template, request, redirect, session, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app import app, login_manager, db
from models import *
import requests, json

login_manager.login_view = 'auth'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login')
def login():
    usr = 'coxagazzo'
    passw = 'nosalt'

    user = User.query.filter_by(username='coxagazzo').first()
    login_user(user)
    return 'Você está logado!' + current_user.username


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Você foi deslogado'

@app.route('/')
def index():
    return render_template('index.html')