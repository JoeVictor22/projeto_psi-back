import functools
from pydantic import BaseModel, ValidationError
from flask import request
import ujson

from aplicativo import app
from aplicativo.components.respostas import Respostas
from aplicativo.messages import mensagens_pydantic
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

# pydantic validator
from aplicativo.models.usuario import Usuario


def field_validator(validator):
    def wrapper(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            data = request.get_data()

            try:
                validator.parse_raw(data)
            except ValidationError as e:
                for error in e.errors():
                    msg = mensagens_pydantic.get(error["type"])
                    ctx = error.get("ctx")

                    if msg:
                        if ctx:
                            msg = msg.format(**ctx)
                        error["msg"] = msg

                validation_errors = {"body_params": e.errors()}

                return (
                    ujson.dumps(
                        {
                            "validation_error": validation_errors,
                            "status_code": 400,
                        }
                    ),
                    400,
                )

            return f(*args, **kwargs)

        return wrapped

    return wrapper


# access control
def checar_acesso(resource_name: str):
    def wrapper(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            try:
                verify_jwt_in_request()
            except Exception:
                return Respostas.erro_generico("erro de autenticacao", codigo=401).json

            user = app.session.get(Usuario, get_jwt_identity())
            if user is None:
                return Respostas.erro_generico("erro de autenticacao", codigo=401).json

            return f(*args, **kwargs)

        return wrapped

    return wrapper
