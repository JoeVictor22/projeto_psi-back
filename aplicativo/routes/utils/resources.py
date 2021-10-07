import ujson
from aplicativo import app


@app.route("/")
def index():
    return ujson.dumps("meu chapadadadddd"), 200


@app.errorhandler(404)
def page_not_found(e):
    return "404 meu chapa", 404
