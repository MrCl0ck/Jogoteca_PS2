import json

def ler():
    with open('caminho/arquivo.json', 'r') as f:
        return json.load(f)

def escrever(objeto):
    with open('caminho/arquivo.json', 'w') as f:
        json.dump(objeto, f)

def ver_json():
    print(ler())