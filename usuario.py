import login
from json_file import UsuarioJSON
from datetime import datetime
from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()

#Caminho para o banco de dados dos usuários cadastrados
__banco_user = './data/user.json'

class Usuario(BaseModel):
    nome: str
    email: str
    data: str = str(datetime.now().date()) #Data atual
    jogos: str = []
    nivel: str = 'Noob'
    pontos: int = 0

@app.get("/private/users/{email}")
def retornar_usuario(email: str):
    usuarios = UsuarioJSON.ler(__banco_user)
    usuarios = usuarios["usuarios"]
    for user in usuarios:
        if(user["email"] == email):
            return user

    return retornar_admin(email)

def retornar_admin(email: str):
    admins = UsuarioJSON.ler(__banco_user)
    admins = admins["admins"]
    for admin in admins:
        if(admin["email"] == email):
            return admin

    return None

@app.get("/private/users")
def listar_usuarios():
    usuarios = UsuarioJSON.ler(__banco_user)
    usuarios = usuarios["usuarios"] #Essa chave é usada, pois dentro dessa chave há um valor onde é armazenado uma lista com todos os usuários 
    for user in usuarios:
        for chave, valor in user.items():
            print(chave,":",valor)

    return usuarios

def criar_usuario(nome: str, email: str):
    UsuarioJSON.escrever(Usuario(nome=nome, email=email),__banco_user)
    return "Usuário criado com sucesso!"

def atualizar_usuario(user: Usuario):
    #Deleta o usuário antigo do banco de dados, após, ele escreve o usuário novamente no banco de dados.

    UsuarioJSON.atualizar(user,__banco_user)

    return "Usuário atualizado com sucesso!"


@app.delete("/private/users/{email}")
def deletar_usuario(email: str):
    usuario = retornar_usuario(email)

    if(usuario == None):
        return "Este usuário não existe!"

    UsuarioJSON.deletar(usuario, __banco_user)# Deleta do banco user todo os valores relacionados a aquele usuário
    login.deletar_login(email)# Deleta do banco login o email e a senha daquele usuário

    return "Usuário deletado com sucesso!"


def adicionar_experiencia(jogo_nome: str, pontos: int, tempo: int, email: str):
    jogo_nome = jogo_nome.lower()
    user = retornar_usuario(email)
    jogos = user["jogos"]
    for jogo in jogos:
        if(jogo["nome"] == jogo_nome):
            jogo["experiencia"]["pontos"] += pontos
            jogo["experiencia"]["tempo"] += tempo
            return atualizar_usuario(user)

    return "Não foi possível adicionar experiência a este jogo"
            