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
    jogos: str = "Você não tem nenhum jogo adicionado!"
    nivel: str = 'Noob'
    pontos: int = 0

@app.get("/private/users/{email}")
def retornar_usuario(email: str):
    usuarios = UsuarioJSON.ler(__banco_user)
    usuarios = usuarios["usuarios"]
    for user in usuarios:
        if(user["email"] == email):
            return user

    return None

@app.get("/private/users")
def listar_usuarios():
    usuarios = UsuarioJSON.ler(__banco_user)
    usuarios = usuarios["usuarios"] #Essa chave é usada, pois dentro dessa chave há um valor onde é armazenado uma lista com todos os usuários 
    for user in usuarios:
        for chave, valor in user.items():
            print(chave,":",valor)

@app.post("/private/users")
def criar_usuario(nome: str, email: str):
    UsuarioJSON.escrever(Usuario(nome=nome, email=email),__banco_user)

@app.delete("/private/users/{email}")
def deletar_usuario(email: str):
    usuario = retornar_usuario(email)

    if(usuario == None):
        return "Este usuário não existe!"

    UsuarioJSON.deletar(usuario, __banco_user)# Deleta do banco user todo os valores relacionados a aquele usuário
    login.deletar_login(email)# Deleta do banco login o email e a senha daquele usuário
