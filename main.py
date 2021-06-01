from flask import Flask, request
from flask.helpers import flash
from flask.templating import render_template
from flask_restful import Api, Resource
import jogos
import login

app = Flask(__name__)
app.secret_key = "jogotecaps2u.?"
api = Api(app)


@app.get("/index")
def index_page():
    return render_template('lista_jogos.html', titulo="Jogoteca - PS2", lista = jogos.retornar_jogos())

@app.get("/login")
def login_page():
    return render_template('login.html', titulo="Login - Jogoteca - PS2")

@app.post("/autenticar")
def autenticar():
    flash(request.form["email"], request.form["senha"])
    res = login.autenticar(request.form["email"], request.form["senha"])

    return res

app.run(debug=True)