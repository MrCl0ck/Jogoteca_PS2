from datetime import datetime
from json_file import JogosJSON
from pydantic.main import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Jogos(BaseModel):
    nome: str
    console: str = "PlayStation 2"
    popularidade: float
    categoria: str
    data: str


#Caminho para o banco de dados dos jogos cadastrados 
__banco_jogos = './data/jogos.json'

#Validação de dados, verifica se já existe um jogo com aquele nome. Sem diferença de maiúsculas e minúsculas
def retornar_jogo(nome: str):
    nome = nome.lower()
    base_de_dados = JogosJSON.ler(__banco_jogos)
    base_de_dados = base_de_dados["jogos"]
    for jogo in base_de_dados:
        for chave, valor in jogo.items():
            print(chave,":",valor)
            if(valor == nome):
                return jogo #Retorna um dicionário contendo as informações do jogo

    return None


#Criação e inserção de um jogo, e suas informações, no banco de dados
#Rota para testes
@app.post("/private/jogos")
def cadastrar_jogo(jogo: dict):
    if(retornar_jogo(jogo["nome"]) != None):
        return "Este jogo já existe!"

    #Passa o nome do jogo em letras minúsculas, para futura conferência
    JogosJSON.escrever(Jogos(nome=jogo["nome"].lower(), popularidade=jogo["popularidade"], categoria=jogo["categoria"], data=jogo["data"]), __banco_jogos)

    return "Jogo cadastrado com sucesso!"

@app.delete("/private/jogos/{nome}")
def deletar_jogo(nome: str):
    jogo = retornar_jogo(nome)
    if(jogo == None):
        return "Este jogo não existe!"

    JogosJSON.deletar(jogo, __banco_jogos)

    return "Jogo deletado com sucesso!"