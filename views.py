from flask import render_template, request, redirect, session, url_for
from flask_login import login_user, logout_user, login_required, current_user
from app import app, login_manager, db
from models import *
import requests, json

login_manager.login_view = 'index'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        formUser = request.form['username']

        user = User.query.filter_by(username=formUser).first()
        login_user(user)
        
        session['username']= current_user.username

        return redirect(url_for('home'))

        # user = User.query.filter_by(username='coxagazzo').first()
        # login_user(user)
        # return 'Você está logado!' + current_user.username


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template('index.html')

    
@app.route('/home')
@login_required
def home():
    return render_template('home.html')