from app import db
from flask_sqlalchemy import Model
from datetime import datetime
from flask_login import UserMixin
from passlib.hash import sha256_crypt as hash

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index = True)
    email = db.Column(db.String(100), nullable=True)
    password_hash = db.Column(db.String(256))
    posts = db.relationship('Post', backref='user', lazy = True)

    __table_args__ = (db.UniqueConstraint('id', 'username'),)

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.password_hash = hash.encrypt(password)

    def verify_password(self, password):
        return (hash.verify(password, self.password_hash))
    
    def __repr__(self):
        return f"id: {id}, username: {username}, email: {email}"

class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.TIMESTAMP)

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id
        self.timestamp = datetime.now()