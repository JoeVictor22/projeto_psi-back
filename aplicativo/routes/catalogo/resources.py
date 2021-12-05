from flask import request
from aplicativo import app
from aplicativo.components.respostas import Respostas
from aplicativo.components.routes import field_validator, checar_acesso
from aplicativo.models.catalogo import Catalogo, CatalogoModel
from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import SQLAlchemyError
from pprint import pprint

prefix = "/catalogo"


@app.route(f"{prefix}/list", methods=["GET"])
@checar_acesso(f"{prefix}-get")
def catalogo_all():

    pagina = request.args.get("pagina", 0) * app.config["POR_PAGINA"]

    query = select(Catalogo)

    if request.args.get("nome", None):
        query = query.where(Catalogo.nome.ilike(f"%{request.args['nome']}%"))

    if request.args.get("email", None):
        query = query.where(Catalogo.perfil_id == {request.args["perfil_id"]})

    query.offset(pagina).limit(app.config["POR_PAGINA"])

    result = app.session.execute(query).scalars().all()
    output = {"count": len(result), "items": list(map(Catalogo.to_dict, result))}

    res = Respostas.retorno_generico(dicionario=output, codigo=200)

    return res.json


@app.route(f"{prefix}/get/<item_id>", methods=["GET"])
@checar_acesso(f"{prefix}-get")
def catalogo_get(item_id):
    result = app.session.get(Catalogo, item_id)
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
@field_validator(CatalogoModel)
def catalogo_add():
    json = request.get_json()
    novo_registro = Catalogo.from_dict(json)

    stmt = insert(Catalogo).values(novo_registro.to_dict())

    try:
        app.session.execute(stmt)
        app.session.commit()
        res = Respostas.mensagem_generica(codigo=200)

    except SQLAlchemyError as e:
        res = Respostas.erro_generico(codigo=400)

    return res.json


@app.route(f"{prefix}/edit/<item_id>", methods=["PUT"])
@checar_acesso(f"{prefix}-put")
@field_validator(CatalogoModel)
def catalogo_edit(item_id):
    json = request.get_json()
    dados_alterados = Catalogo.to_update(json)

    stmt = update(Catalogo).where(Catalogo.id == item_id).values(**dados_alterados)

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
def catalogo_delete(item_id):
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
            content:
                application/json:
                    schema:
                        $ref: "#/components/schemas/CatalogoModel"
    """
    stmt = delete(Catalogo).where(Catalogo.id == item_id)

    try:
        app.session.execute(stmt)
        app.session.commit()
        res = Respostas.mensagem_generica(codigo=200)

    except SQLAlchemyError as e:
        print(e)
        res = Respostas.erro_generico(codigo=400)

    return res.json
