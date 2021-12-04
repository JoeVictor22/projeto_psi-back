from flask import request
from aplicativo import app
from aplicativo.components.respostas import Respostas
from aplicativo.components.routes import field_validator, checar_acesso
from aplicativo.models.usuario import Usuario, UsuarioModel
from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import SQLAlchemyError
from pprint import pprint

prefix = "/usuario"


@app.route(f"{prefix}/list", methods=["GET"])
@checar_acesso(f"{prefix}-get")
def usuario_all():

    pagina = request.args.get("pagina", 0) * app.config["por_pagina"]

    query = select(Usuario)

    if request.args.get("nome", None):
        query.where(Usuario.nome.ilike(f"%{request.args['nome']}%"))

    if request.args.get("email", None):
        query.where(Usuario.email.ilike(f"%{request.args['email']}%"))

    if request.args.get("grupo_id", None):
        query.where(Usuario.grupo_id == request.args.get["grupo_id"])

    query.offset(pagina).limit(app.config["por_pagina"])

    result = app.session.execute(query).scalars().all()
    output = {"count": len(result), "items": list(map(Usuario.to_dict, result))}

    res = Respostas.retorno_generico(dicionario=output, codigo=200)

    return res.json


@app.route(f"{prefix}/get/<item_id>", methods=["GET"])
@checar_acesso(f"{prefix}-get")
def usuario_get(item_id):
    result = app.session.get(Usuario, item_id)
    pprint(result)

    if not result:
        res = Respostas.mensagem_generica(
            mensagem="Não foi possivel encontrar o registro", codigo=204
        )
        return res.json

    output = {**result.to_dict()}

    res = Respostas.retorno_generico(dicionario=output, codigo=200)
    return res.json


@app.route(f"{prefix}/add", methods=["POST"])
@checar_acesso(f"{prefix}-post")
@field_validator(UsuarioModel)
def usuario_add():
    json = request.get_json()
    novo_registro = Usuario.from_dict(json)

    stmt = insert(Usuario).values(novo_registro.to_dict())

    try:
        app.session.execute(stmt)
        app.session.commit()
        res = Respostas.mensagem_generica(codigo=200)

    except SQLAlchemyError as e:
        res = Respostas.erro_generico(codigo=400)

    return res.json


@app.route(f"{prefix}/edit/<item_id>", methods=["PUT"])
@checar_acesso(f"{prefix}-put")
@field_validator(UsuarioModel)
def usuario_edit(item_id):
    json = request.get_json()
    dados_alterados = Usuario.to_update(json)

    stmt = update(Usuario).where(Usuario.id == item_id).values(**dados_alterados)

    try:
        app.session.execute(stmt)
        app.session.commit()
        res = Respostas.mensagem_generica(codigo=200)

    except SQLAlchemyError as e:
        print(e)
        res = Respostas.erro_generico(codigo=400)

    return res.json


@app.route(f"{prefix}/delete/<item_id>", methods=["delete"])
@checar_acesso(f"{prefix}-delete")
def usuario_delete(item_id):
    """Gist detail view.
        ---
        get:
          summary: Get a user by ID
          parameters:
            - in: path
              name: item_id
              schema:
                type: integer
              required: true
              description: Numeric ID of the user to get
          responses:
            200:
                "description": "pong"
    """
    stmt = delete(Usuario).where(Usuario.id == item_id)

    try:
        app.session.execute(stmt)
        app.session.commit()
        res = Respostas.mensagem_generica(codigo=200)

    except SQLAlchemyError as e:
        print(e)
        res = Respostas.erro_generico(codigo=400)

    return res.json