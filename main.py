from datetime import timedelta
from flask import Flask, request, session
from flask.templating import render_template
from flask_restful import Api, Resource
from werkzeug.utils import redirect
from flask.helpers import url_for
import login, usuario, jogos

app = Flask(__name__)
app.secret_key = "jogotecaps2u.?"
api = Api(app)

@app.get("/sessao")
def retornar_sessao():
    #Caso exista a chave "logado" ele irá retornar esse valor dentro da chave. Caso não exista a chave "logado" ele irá retornar "não logado"
    user = session.get('logado', 'não logado')

    #Verifica se um admin que está logado
    if(user == "não logado"):
        user = session.get('admin', 'não logado')
    
    return user
    
@app.get("/")
@app.get("/index")
def index_page():
    return render_template('lista_jogos.html', titulo="Jogoteca - PS2", lista = jogos.retornar_jogos(), sessao = retornar_sessao())

@app.get("/login")
def login_page():
    return render_template('login.html', titulo="Login - Jogoteca - PS2")

@app.post("/autenticar")
def autenticar():
    res = login.autenticar(request.form["email"], request.form["senha"])

    if(res == None):
        return "Email e/ou senha incorretos!"

    return redirect(url_for('dashboard'))

@app.get("/dashboard")
def dashboard():
    return render_template('dashboard.html', user = usuario.retornar_usuario(retornar_sessao()))
    

@app.get("/experiencia")
def experiencia():
    return render_template('cad_experiencia.html', titulo = "Cadastrar Experiência")

@app.get("/logout")
def logout():
    session.clear()
    #Mensagem para avisar que saiu!
    return redirect(url_for("index_page"))

app.run(debug=True)