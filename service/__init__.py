from flask import Flask
import ujson
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

def config_db():
    load_dotenv()
    return os.getenv(
        "DATABASE", "postgresql://postgres:admin@localhost/banco_teste"
    )


app = Flask(__name__)
# app.config.from_object("infra/config")
app.config["SQLALCHEMY_DATABASE_URI"] = config_db()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True



db = SQLAlchemy(app)
migrate = Migrate(app, db)

import service.models

@app.route("/")
def index():
    print("q")
    return ujson.dumps("index")
