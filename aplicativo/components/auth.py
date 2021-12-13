import ujson
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
)
from flask import request
from sqlalchemy import select
from werkzeug.security import check_password_hash

from aplicativo import app
from aplicativo.components.respostas import Respostas
from aplicativo.components.routes import field_validator
from aplicativo.models.usuario import Usuario
from aplicativo.models.utils.Auth import AuthSchema


@app.route("/auth", methods=["POST"])
@field_validator(AuthSchema)
def login():
    """Cria chave JWT para acesso"""
    data = request.get_json()

    usuario = select(Usuario).where(Usuario.email == data["email"]).limit(1)

    if not usuario:  # no authorization
        return Respostas.erro_generico("usuario inexistente", codigo=401).json

    elif not check_password_hash(usuario.senha, str(data.get("senha"))):
        return Respostas.erro_generico("erro de autenticacao", codigo=401).json

    # Todo create hash for id
    return (
        ujson.dumps(
            {
                "access_token": create_access_token(identity=usuario.id),
                "refresh_token": create_refresh_token(identity=usuario.id),
            }
        ),
        200,
    )


@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    usuario = get_jwt_identity()

    return (
        ujson.dumps({"access_token": create_access_token(identity=usuario)}),
        200,
    )
