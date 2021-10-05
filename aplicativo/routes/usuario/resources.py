import ujson
from aplicativo import app
from aplicativo.models.usuario import Usuario, UsuarioModel
from sqlalchemy import select
from pprint import pprint

prefix = "/usuario"

@app.route(f"{prefix}/all", methods=["GET"])
def usuario_all():

    # select(Usuario)
    # result1 = app.session.execute(select).scalars().all()
    # result2 = app.session.execute(select).all()
    #
    # pprint(result1)
    # pprint(result2)

    result1 = app.session.query(Usuario).all()
    result = list(map(UsuarioModel.from_orm, result1))

    pprint(result)

    return ujson.dumps("b"), 200

