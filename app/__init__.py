from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)


# app.run(debug=True)

from app.routes import *