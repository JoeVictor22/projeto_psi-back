import ujson
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
)
from flask import request

from aplicativo import app


@app.route("/auth", methods=["POST"])
# @field_validator(AuthLoginSchema)
def login():
    """Cria chave JWT para acesso"""
    data = request.get_json()

    if False:  # no authorization
        return ujson.dumps("erro"), 401

    return (
        ujson.dumps(
            {
                "access_token": create_access_token("id_do_user_ou_chave"),
                "refresh_token": create_refresh_token("id_do_user_ou_chave"),
            }
        ),
        200,
    )


@app.route("/refresh", methods=["POST"])
#@jwt_required(refresh=True)
def refresh():
    # current_user = get_jwt_identity()
    current_user = "o_id_chave_do_usuario"

    return (
        ujson.dumps({"access_token": create_access_token(identity=current_user)}),
        200,
    )


# --------------------------------------------------------------------------------------------------#


@app.route("/me", methods=["GET"])
#@jwt_required
def me():
    current_user = get_jwt_identity()

    user = "checa se o registro ta no banco"

    if user is None:
        return ujson.dumps({"message": "msg de erro", "error": True})

    return (
        ujson.dumps({"todas_as_infos_do_usuario", "infos"}),
        200,
    )
