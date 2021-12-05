from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
import json

from aplicativo import app
from aplicativo.routes.usuario.resources import usuario_delete, usuario_edit, usuario_add, usuario_get, usuario_all
from aplicativo.models.usuario import UsuarioModel

spec = APISpec(
    title="Backend",
    version="1.0.0",
    openapi_version="3.0.2",
    info=dict(
        description="API backend para aplicação",
        version="1.0.0-oas3",
        contact=dict(
            email="joelvictor1746@gmail.com"
            ),
        ),
    servers=[
        dict(
            description="Server local",
            url="http://localhost:5000"
            )
        ],
    tags=[
        dict(
            name="Rotas",
            description="Rotas"
            )
        ],
    plugins=[FlaskPlugin()],
)



with app.app_context():



    f = open("../utils/out.txt", "w")
    f.write(json.dumps(spec.to_dict(),indent=4))
    f.close()
    # models = [UsuarioModel.schema()]
    # for model in models:
    #     app.componentes.schemas('Usuario', model)

    ref = UsuarioModel.schema()
    spec.components.schema(ref['title'], ref)
    
    spec.path(view=usuario_delete)
    spec.path(view=usuario_all)
    spec.path(view=usuario_get)
    spec.path(view=usuario_add)
    spec.path(view=usuario_edit)

    f = open("../utils/out.json", "w")
    f.write(json.dumps(spec.to_dict(), indent=4))
    f.close()

