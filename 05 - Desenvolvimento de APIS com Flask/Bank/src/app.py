from flask import Flask, request, url_for, Request

app = Flask(__name__)


@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    print(altura)
    print(idade)
    print(f'tipo da varealvel altura{type(altura)}')
    print(f'tipo da variavel idade{type(idade)}')
    print(f'tipo da variavel usuario{type(usuario)}')
    return f"<h1>OLÁ!: {usuario.upper()}</h1>"

@app.route("/bomdia")
def Bom_dia():
    return "<h1>Bom Dia!!!</h1>"

@app.route("/projects/")
def projects():
    return "The project page"


@app.route("/about", methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        return 'this is a GET'
    else:
        return'this is a POST'


with app.test_request_context():
    print(url_for('Bom_dia'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('hello_world',usuario='Felipe',idade=24, altura=1.66))
