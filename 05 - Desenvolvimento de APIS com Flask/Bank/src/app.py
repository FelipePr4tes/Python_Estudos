from flask import Flask

app = Flask(__name__)


@app.route("/olamundo")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bomdia")
def Bom_dia():
    return "<h1>Hello, World!</h1>"