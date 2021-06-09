from dotenv import load_dotenv
from dynaconf import FlaskDynaconf
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads

load_dotenv()

app = Flask(__name__)
flask_dynaconf = FlaskDynaconf(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'Please log in to access this page'

imagefiles = UploadSet('images', IMAGES)
configure_uploads(app, imagefiles)

from app import routes, models, errors
