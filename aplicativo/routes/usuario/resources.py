from flask import request
import ujson
from aplicativo import app
from aplicativo.components.routes import field_validator, checar_acesso
from aplicativo.models.usuario import Usuario, UsuarioModel
from sqlalchemy import select, insert, update, delete
from pprint import pprint

prefix = "/usuario"


@app.route(f"{prefix}/list", methods=["GET"])
# @checar_acesso("usuario-get")
def usuario_all():
    query = select(Usuario)
    result = app.session.execute(query).scalars().all()
    output = {
        "count": len(result),
        "items": list(map(Usuario.to_dict, result))
    }

    return ujson.dumps(output), 200


@app.route(f"{prefix}/get/<item_id>", methods=["GET"])
# @checar_acesso("usuario-get")
def usuario_get(item_id):
    result = app.session.get(Usuario, item_id)
    pprint(result)

    if not result:
        return ujson.dumps("fail"), 200

    output = {
        **result.to_dict()
    }
    return ujson.dumps(output), 200


@app.route(f"{prefix}/add", methods=["POST"])
# @checar_acesso("usuario-post")
@field_validator(UsuarioModel)
def usuario_add():
    json = request.get_json()
    novo_registro = Usuario.from_dict(json)

    stmt = insert(Usuario).values(novo_registro.to_dict())

    try:
        app.session.execute(stmt)
        app.session.commit()
        message = "sucesso"
    except Exception as e:
        print(e)
        message = "falha"

    return ujson.dumps(message), 200


@app.route(f"{prefix}/edit/<item_id>", methods=["PUT"])
# @checar_acesso("usuario-put")
@field_validator(UsuarioModel)
def usuario_edit(item_id):
    json = request.get_json()
    dados_alterados = Usuario.to_update(json)

    stmt = update(Usuario).where(Usuario.id == item_id).values(**dados_alterados)

    try:
        app.session.execute(stmt)
        app.session.commit()
        message = "sucesso"
    except Exception as e:
        print(e)
        message = "falha"

    return ujson.dumps(message), 200


@app.route(f"{prefix}/delete/<item_id>", methods=["delete"])
# @checar_acesso("usuario-delete")
def usuario_delete(item_id):
    stmt = delete(Usuario).where(Usuario.id == item_id)

    try:
        app.session.execute(stmt)
        app.session.commit()

        message = "sucesso"
    except Exception as e:
        print(e)
        message = "falha"

    return ujson.dumps(message), 200
