from fastapi import FastAPI
from pydantic import BaseModel


#Modelo da classe usuário
class Usuario(BaseModel):
    nome: str
    email: str
    data: str
    jogos: object
    nivel: str = None #não requisitado
    pontos: int = None #não requisitado

#Validação de dados (email, pois o email é o login!)
def validar(email: str):
    



    
        