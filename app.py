from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config.from_object('config.DevConfig')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

#app precisa ser criado antes de importar views e models
from views import *
from models import *

db.drop_all()
db.create_all()

temp = User(username = 'coxagazzo', password='nosalt', email='a@b.com')
db.session.add(temp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')