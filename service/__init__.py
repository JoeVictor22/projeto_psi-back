from flask import Flask
import ujson
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

service = Flask(__name__)
service.config.from_object("infra/config")
db = SQLAlchemy(service)
migrate = Migrate(service, db)

import models

@service.route("/")
def index():
    print("q")
    return ujson.dumps("index")
