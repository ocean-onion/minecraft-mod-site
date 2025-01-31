from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from models import User, Plugin
import routes

if __name__ == "__main__":
    app.run(debug=True)
