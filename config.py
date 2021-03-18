import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # BASE CONFIG
    SECRET_KEY = '%yaoroe$abifz4%58yd1kxea6j&2y13i!3dby0wo)i0nmwxyne'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_DATABASE_URI = 'postgresql://rwxrlxtdwqwhty:4f8fc71f49122543961fc37e42d28cab04eb85d55668f0b27f89c60e79039b97@ec2-52-44-31-100.compute-1.amazonaws.com:5432/d9jaaiuhudnj62'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'false'

class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    TESTING = True