import usuario 
from json_file import LoginJSON
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Caminho para o banco de dados dos logins e senhas cadastrados
__banco_login = "./data/login.json"

#Modelo da classe Login
class Login(BaseModel):
    nome: str
    email: str

#Retornar um usuário
#Validação de dados (email, pois o email é o login!)
def retornar_login(email: str):
    logins = LoginJSON.ler(__banco_login)
    logins = logins["logins"]
    for cadastro in logins:
        if(email in cadastro):
            return cadastro #retorna um dicionário, que é o "login/email" na chave e a "senha" no valor da chave

    return None

#Faz a autenticação do login e senha passados
#FALTA - ROTA AUTENTICAR
def autenticar(email:str, senha: str):
    logins = LoginJSON.ler(__banco_login)
    for login, senha_login in logins.items():
        if(login == email):
            if(senha_login == senha):
                return "Logando..."
            else:
                return "E-mail e/ou senha incorretos!"
        else:
            return "Este e-mail não existe!"

     
#Criação e inserção de um login e senha no banco de dados
@app.post("private/users")
def criar_login(email: str, senha: str, nome: str):
    if(retornar_login(email) != None):
        return "E-mail já existente!"

    LoginJSON.escrever(Login(email= email, senha= senha), __banco_login)
    usuario.criar_usuario(nome, email) #Método do arquivo usuario.py

    return "Usuário cadastrado com sucesso!"
    
#Deletar um login e senha do banco de dados
def deletar_login(email: str):
    login = retornar_login(email)

    if(login == None):
        return "Este usuário não existe!"

    LoginJSON.deletar(login, __banco_login)



    
        