from flask import render_template, request, redirect, session, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, login_manager, db
from models import *
import requests, json

login_manager.login_view = 'index'


# TESTANDO BRANCH

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        formUser = request.form['username']
        formPass = request.form['password']

        user = User.query.filter_by(username=formUser).first()

        if (user is not None):
            if (user.verify_password(formPass)):
                login_user(user)
                session['username']= current_user.username
                return redirect(url_for('home'))
            else:
                flash('Senha incorreta!')
                return redirect(url_for('index'))
        flash('Usuário inválido')
        return redirect(url_for('index'))
        # user = User.query.filter_by(username='coxagazzo').first()
        # login_user(user)
        # return 'Você está logado!' + current_user.username

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
        
    if request.method == 'POST':
        usuario = request.form['username']
        senha = request.form['password']
        email = request.form['email']

        if ( User.query.filter_by(username=usuario).first() is not None ):
            flash('Usuário não disponivel')
            return redirect(url_for('register'))

        new_user = User(usuario, senha, email)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        session['username']= current_user.username

        return redirect(url_for('home'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session['username']= None
    return redirect(url_for('index'))

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template('index.html')

    
@app.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    post = Post(text=request.form['postInput'], user_id=current_user.id)
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/u/<username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username = username).first()
    posts = Post.query.filter_by(user_id = user.id).all()

    return render_template('user.html', posts=posts, user=user)

@app.route('/home')
@login_required
def home():

    posts = Post.query.filter_by(user_id=current_user.id).all()

    return render_template('home.html', posts = posts)