from flask import Flask, _app_ctx_stack
from flask_cors import CORS
from flask_jwt_extended import JWTManager

import infra.config as config
from sqlalchemy.orm import scoped_session
from aplicativo.database import SessionLocal, engine, Base
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

app.config.from_object(config)
jwt = JWTManager(app)

CORS(app)  # se o deploy for em vpc ou de msm origem, remover cors

app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)


import aplicativo.routes
import aplicativo.models

Base.metadata.create_all(bind=engine)


@app.teardown_appcontext
def close_session(e):
    app.session.remove()
