import functools
from pydantic import BaseModel, ValidationError
from flask import request
import ujson
from aplicativo.messages import mensagens_pydantic
from flask_jwt_extended import get_jwt_identity, jwt_required

# pydantic validator
def field_validator(validator: BaseModel):
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
def checar_acesso(resource_name: str):  # passar o nome da rota
    #@jwt_required
    def wrapper(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            return f(*args, **kwargs)

            user = get_jwt_identity()  # consultar no banco com a chave
            if user is None:
                return (
                    ujson.dumps(
                        {
                            "description": "messagem usuario negado",
                            "error": "Unauthorized Access",
                            "status_code": 401,
                        }
                    ),
                    401,
                )

            # user_role = user.cargo_id
            # contr, act = resource_name.split("-")

            data = "registro com as informacoes da rota do sistema"

            if data is None:
                return (
                    ujson.dumps(
                        {
                            "description": "mensagem de ACESSO NEGADO",
                            "error": "Unauthorized Access",
                            "status_code": 401,
                        }
                    ),
                    401,
                )

            if not data.permitir:
                return (
                    ujson.dumps(
                        {
                            "description": "mensagem ACESSO NEGADO",
                            "error": "Unauthorized Access",
                            "status_code": 401,
                        }
                    ),
                    401,
                )

            return f(*args, **kwargs)

        return wrapped

    return wrapper
