from json_file import UsuarioJSON
from typing import Any
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
    jogos: Any = "Você não tem nenhum jogo adicionado!"
    nivel: str = 'Noob'
    pontos: int = 0

@app.get("/private/users")
def retornar_usuarios():
    usuarios = UsuarioJSON.ler(__banco_user)
    usuarios = usuarios["usuarios"] #Essa chave é usada, pois dentro dessa chave há um valor onde é armazenado uma lista com todos os usuários 
    for user in usuarios:
        for chave in user:
            print(chave,":",user[chave])

@app.post("/private/users")
def criar_usuario(email_p: str, nome_p: str):
    UsuarioJSON.escrever(Usuario(nome=nome_p, email=email_p),__banco_user)

