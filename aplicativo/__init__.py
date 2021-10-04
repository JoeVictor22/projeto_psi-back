from flask import Flask, _app_ctx_stack
from flask_cors import CORS
import infra.config as config
from sqlalchemy.orm import scoped_session
from aplicativo.database import SessionLocal, engine, Base

app = Flask(__name__)
app.config.from_object(config)

CORS(app)  # se o deploy for em vpc ou de msm origem, remover cors

app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)


import aplicativo.routes
import aplicativo.models

Base.metadata.create_all(bind=engine)


@app.teardown_appcontext
def close_session(e):
    app.session.remove()
