from typing import Any
from json_file import ler
from fastapi import FastAPI
from pydantic import BaseModel


#Modelo da classe usuário
class Usuario(BaseModel):
    nome: str
    email: str
    data: str
    jogos: Any
    nivel: str #não requisitado
    pontos: int #não requisitado


s = Usuario(nome='ase',email='ase@ase.com.br',data='27/05/2021',jogos={}, nivel="Mestre", pontos=100)

#Validação de dados (email, pois o email é o login!)
def validar(email):
    logins = ler("./data/login.json")
    for login, senha in logins.items():
        print(login,": ",senha)
        if(login == email):
            return "E-mail já existente!"

    return "E-mail disponível!"

    
        