from flask import Flask
import ujson

service = Flask("service")

@service.route("/")
def index():
    return ujson.dumps("index")
