from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
import json

from aplicativo import app
from aplicativo.routes.usuario.resources import (
    usuario_delete,
    usuario_edit,
    usuario_add,
    usuario_get,
    usuario_all,
)
from aplicativo.models.usuario import UsuarioModel

from aplicativo import app
from aplicativo.routes.produto.resources import (
    produto_delete,
    produto_edit,
    produto_add,
    produto_get,
    produto_all,
)
from aplicativo.models.produto import ProdutoModel

from aplicativo.routes.perfil.resources import (
    perfil_delete,
    perfil_edit,
    perfil_add,
    perfil_get,
    perfil_all,
)
from aplicativo.models.perfil import PerfilModel
from aplicativo.enumerators.cidade import CidadeModel

spec = APISpec(
    title="Backend",
    version="1.0.0",
    openapi_version="3.0.2",
    info=dict(
        description="API backend para aplicação",
        version="1.0.0-oas3",
        contact=dict(email="joelvictor1746@gmail.com"),
    ),
    servers=[dict(description="Server local", url="http://localhost:5000")],
    tags=[dict(name="Rotas", description="Rotas")],
    plugins=[FlaskPlugin()],
)


with app.app_context():

    f = open("../utils/out.txt", "w")
    f.write(json.dumps(spec.to_dict(), indent=4))
    f.close()
    models = [
        PerfilModel.schema(),
        ProdutoModel.schema(),
        UsuarioModel.schema(),
        CidadeModel.schema(),
    ]
    # del models[0]['definitions']
    # models[0]['properties']['cidade_id']['$ref'] = '#/components/schemas/CidadeModel'
    for model in models:
        spec.components.schema(model["title"], model)

    paths = [
        perfil_delete,
        perfil_all,
        perfil_get,
        perfil_add,
        perfil_edit,
        produto_delete,
        produto_all,
        produto_get,
        produto_add,
        produto_edit,
        usuario_delete,
        usuario_all,
        usuario_get,
        usuario_add,
        usuario_edit,
    ]
    for path in paths:
        spec.path(view=path)

    f = open("../utils/out.json", "w")
    f.write(json.dumps(spec.to_dict(), indent=4))
    f.close()
