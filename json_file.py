import json
from usuario import Usuario

class GeralJSON:
    def ler(caminho):
        with open(caminho, 'r') as f:
            return json.load(f)

    def escrever(objeto, caminho):
        with open(caminho, 'a') as f:
            return json.dump(objeto, f)


class LoginJSON:
    def ler(caminho):
        with open(caminho, 'r') as f:
            return json.load(f)

    def escrever(email, senha, caminho):
        #Lê o banco antes do método open, pois como o modo está write e ele apaga tudo quando o método open é chamado
        banco_usuario = LoginJSON.ler(caminho)
        with open(caminho, 'w') as f:
            #Insere o email na chave e no valor coloca a senha, ambos passados por parâmetro
            banco_usuario[email] = senha
            return json.dump(banco_usuario, f)


class UsuarioJSON:
    def ler(caminho):
        with open(caminho, 'r') as f:
            return json.load(f)

    def escrever(usuario: Usuario, caminho):
        with open(caminho, 'w') as f:
            pass