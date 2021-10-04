from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import infra.config as config

app = Flask(__name__)
app.config.from_object(config)


db = SQLAlchemy(app)


migrate = Migrate(app, db)

import aplicativo.models
import aplicativo.routes
