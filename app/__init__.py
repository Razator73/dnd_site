from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import AppConfig

app = Flask(__name__)
app.config.from_object(AppConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
