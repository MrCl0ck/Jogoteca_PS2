from typing import Any
from usuario import Usuario
from json_file import LoginJSON, UsuarioJSON
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
    for login, senha in logins.items():
        if(login == email):
            return "E-mail já existente!"

    return "E-mail disponível!"

#Faz a autenticação do login e senha passados
def autenticar(email:str, senha: str):
    logins = LoginJSON.ler(__banco)
    for login, senha_login in logins.items():
        if(login == email):
            if(senha_login == senha):
                return "Logando..."
            else:
                return "E-mail e/ou senha incorretos!"
        else:
            return "Este e-mail não existe!"


def ler_usuarios():
    banco = './data/user.json'
    usuarios = UsuarioJSON.ler(banco)
    usuarios = usuarios['usuarios']
    index = 0
    for user in usuarios[index]: #aqqqq
        print(user,": ",)
        index+=1

#Criação e inserção de um login e senha no banco de dados
def criar_login(email: str, senha: str, nome: str):
    if(validar(email) == "E-mail já existente!"):
        return "E-mail já existente!"

    LoginJSON.escrever(email, senha, __banco)    
    UsuarioJSON.escrever(Usuario(nome=nome, email=email))

    return "Usuário cadastrado com sucesso!"
    



    
        