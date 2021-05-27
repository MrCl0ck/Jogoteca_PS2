from typing import Any
from datetime import datetime

from pydantic.main import BaseModel

class Usuario(BaseModel):
    nome: str
    email: str
    data: str = str(datetime.now().date()) #Data atual
    jogos: Any = "Você não tem nenhum jogo adicionado!"
    nível: str = 'Noob'

