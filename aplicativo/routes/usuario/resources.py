from flask import request
import ujson
from aplicativo import app
from aplicativo.components.routes import field_validator, checar_acesso
from aplicativo.models.usuario import Usuario, UsuarioModel
from sqlalchemy import select, insert, update, delete
from pprint import pprint

prefix = "/usuario"


@app.route(f"{prefix}/all", methods=["GET"])
@checar_acesso("usuario-get")
def usuario_all():

    a = select(Usuario)
    result = app.session.execute(a).scalars().all()
    pprint(result)
    result = list(map(UsuarioModel.from_orm, result))

    print("\n")
    pprint(result)

    return ujson.dumps("b"), 200


@app.route(f"{prefix}/view/<item_id>", methods=["GET"])
@checar_acesso("usuario-get")
def usuario_get(item_id):
    result = app.session.get(Usuario, item_id)
    print("\n")
    pprint(result)

    if not result:
        ujson.dumps("fail"), 200

    return ujson.dumps("success"), 200


@app.route(f"{prefix}/add", methods=["POST"])
@checar_acesso("usuario-post")
@field_validator(UsuarioModel)
def usuario_add():
    json = request.get_json()
    novo_registro = Usuario.from_json(json)

    stmt = insert(Usuario).values(**novo_registro)

    try:
        app.session.execute(stmt)
        message = "sucesso"
    except Exception as e:
        print(e)
        message = "falha"

    return ujson.dumps(message), 200


@app.route(f"{prefix}/edit/<item_id>", methods=["PUT"])
@checar_acesso("usuario-put")
@field_validator(UsuarioModel)
def usuario_edit(item_id):
    json = request.get_json()

    dados_alterados = Usuario.from_json(json).to_dict()

    stmt = update(Usuario).where(Usuario.id == item_id).values(**dados_alterados)

    try:
        app.session.execute(stmt)
        message = "sucesso"
    except Exception as e:
        print(e)
        message = "falha"

    return ujson.dumps(message), 200


@app.route(f"{prefix}/edit/<item_id>", methods=["delete"])
@checar_acesso("usuario-delete")
def usuario_delete(item_id):
    stmt = delete(Usuario).where(Usuario.id == item_id)

    try:
        app.session.execute(stmt)
        message = "sucesso"
    except Exception as e:
        print(e)
        message = "falha"

    return ujson.dumps(message), 200
