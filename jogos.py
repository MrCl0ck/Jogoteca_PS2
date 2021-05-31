from datetime import datetime
from pydantic.main import BaseModel

class Jogos(BaseModel):
    nome: str
    console: str = "PlayStation 2"
    popularidade: float
    categoria: str
    data: str(datetime.now().date()) #Retorna data atual

