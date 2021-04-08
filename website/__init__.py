from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import json

with open('secrets.json') as f:
  data = json.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = data['secret_key']

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_EXTENSIONS'] = ['.txt']

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from website import routes