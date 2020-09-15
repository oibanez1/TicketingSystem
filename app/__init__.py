from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


from app.routes import *
from app.models.models import *