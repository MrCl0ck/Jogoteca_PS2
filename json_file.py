import json

def ler(caminho):
    with open(caminho, 'r') as f:
        return json.load(f)

def escrever(objeto, caminho):
    with open(caminho, 'w') as f:
        json.dump(objeto, f)

def ver_json():
    print(ler())