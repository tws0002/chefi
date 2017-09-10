from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
mail = Mail(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models