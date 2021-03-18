from app import db
from flask_sqlalchemy import Model
from flask_login import UserMixin

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index = True)
    email = db.Column(db.String(100), nullable=True)
    password_hash = db.Column(db.String(128))

    __table_args__ = (db.UniqueConstraint('id', 'username'),)
    
    def __repr__(self):
        return f"id: {id}, username: {username}, email: {email}"
