from typing import Any
from json_file import LoginJSON
from fastapi import FastAPI
from pydantic import BaseModel

#Caminho para o banco de dados dos logins e senhas cadastrados
__banco = "./data/login.json"

#Modelo da classe Login
class Login(BaseModel):
    nome: str
    email: str

#Validação de dados (email, pois o email é o login!)
def validar(email: str):
    logins = LoginJSON.ler(__banco)
    print(logins)
    for login, senha in logins.items():
        print(login,": ", senha)
        if(login == email):
            return "E-mail já existente!"

    return "E-mail disponível!"

usuario = {"email": "senha"}
#Criação e inserção de um login e senha no banco de dados
def criar(email: str, senha: str):
    if(validar(email) == "E-mail já existente!"):
        return "E-mail já existente!"

    LoginJSON.escrever(email, senha, __banco)

    return "Usuário cadastrado com sucesso!"
    




    
        