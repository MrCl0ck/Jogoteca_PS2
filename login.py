import usuario
from flask import session
from json_file import LoginJSON
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Caminho para o banco de dados dos logins e senhas cadastrados
__banco_login = "./data/login.json"

#Modelo da classe Login
class Login(BaseModel):
    email: str
    senha: str

#Retornar um usuário
#Validação de dados (email, pois o email é o login!) Sem diferença de maiúsculas e minúsculas
def retornar_login(email: str):
    email = email.lower()
    base_de_dados = LoginJSON.ler(__banco_login)
    base_de_dados = base_de_dados["logins"]
    for login in base_de_dados:
        for chave, valor in login.items():
            if(valor == email):
                return login #retorna um dicionário, que é o "login/email" na chave e a "senha" no valor da chave

    return None

#Faz a autenticação do login e senha passados
def autenticar(email:str, senha: str):
    base_de_dados = LoginJSON.ler(__banco_login)
    base_de_dados = base_de_dados["logins"]
    for login in base_de_dados:
        if(login["email"] == email):
            if(login["senha"] == senha):
                session['logado'] = email
                return login
            else:
                return None
        else:
            return None

     
#Criação e inserção de um login e senha no banco de dados
def criar_login(email: str, senha: str, nome: str):
    if(retornar_login(email) != None):
        return "E-mail já existente!"

    LoginJSON.escrever(Login(email=email, senha=senha), __banco_login)
    usuario.criar_usuario(nome, email) #Método do arquivo usuario.py

    return "Usuário cadastrado com sucesso!"
    
#Deletar um login e senha do banco de dados
def deletar_login(email: str):
    login = retornar_login(email)

    if(login == None):
        return "Este usuário não existe!"

    LoginJSON.deletar(login, __banco_login)



    
        