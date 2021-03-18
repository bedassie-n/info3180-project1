from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

app = Flask(__name__)
app.config.from_object(Config)
from app import views