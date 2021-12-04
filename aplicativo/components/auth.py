import ujson
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
)
from flask import request
from sqlalchemy import select

from aplicativo import app
from aplicativo.components.routes import field_validator
from aplicativo.models.usuario import Usuario
from aplicativo.models.utils.Auth import AuthSchema


@app.route("/auth", methods=["POST"])
@field_validator(AuthSchema)
def login():
    """Cria chave JWT para acesso"""
    data = request.get_json()

    usuario = select(Usuario).where(Usuario.email == data['email'])

    if not usuario:  # no authorization
        return ujson.dumps("erro"), 401 # Todo

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


# --------------------------------------------------------------------------------------------------#


@app.route("/me", methods=["GET"])
@jwt_required
def me():
    usuario_id = get_jwt_identity()

    usuario = app.session.get(Usuario, usuario_id)

    if usuario is None:
        # Todo
        return ujson.dumps({"message": "msg de erro", "error": True})

    return (
        # Todo
        ujson.dumps({"todas_as_infos_do_usuario", "infos"}),
        200,
    )
