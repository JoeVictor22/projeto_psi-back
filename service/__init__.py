from flask import Flask
import ujson
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import infra.config as config

app = Flask(__name__)
app.config.from_object(config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

import service.models





@app.route("/")
def index():
    print("q")
    return ujson.dumps("meu chapadadadddd")
