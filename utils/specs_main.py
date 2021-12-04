from apispec import APISpec
from apispec_webframeworks.flask import FlaskPlugin
import json

from aplicativo import app
from aplicativo.routes.usuario.resources import usuario_delete

spec = APISpec(
    title="Demo API",
    version="1.0.0",
    openapi_version="3.0.2",
    info=dict(
        description="Demo API",
        version="1.0.0-oas3",
        contact=dict(
            email="admin@donofden.com"
            ),
        license=dict(
            name="Apache 2.0",
            url='http://www.apache.org/licenses/LICENSE-2.0.html'
            )
        ),
    servers=[
        dict(
            description="Test server",
            url="https://resources.donofden.com"
            )
        ],
    tags=[
        dict(
            name="Demo",
            description="Endpoints related to Demo"
            )
        ],
    plugins=[FlaskPlugin()],
)



with app.app_context():
    spec.path(view=usuario_delete)
    f = open("../utils/out.txt", "w")
    f.write(json.dumps(spec.to_dict(),indent=4))
    f.close()