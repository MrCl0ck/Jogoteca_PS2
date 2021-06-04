import json

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
            return json.load(f)#retorna os valores dentro da chave "logins", em que está uma lista!!

    def escrever(login: dict, caminho):
        #Caso a escolha seja acrescentar um login no banco de dados
        #Lê o banco antes do método open, pois como o modo está write e ele apaga tudo quando o método open é chamado
        banco_login = LoginJSON.ler(caminho)
        with open(caminho, 'w') as f:
            #Insere o email na chave e no valor coloca a senha, ambos passados por parâmetro
            banco_login["logins"].append(login.dict(include={"email", "senha"}))
            return json.dump(banco_login, f)

    def deletar(login: dict, caminho):
        #Caso a escolha seja deletar um login do banco de dados
        banco_login = LoginJSON.ler(caminho)
        banco_login["logins"].remove(login)
        with open(caminho, 'w') as f:
            print(banco_login)
            return json.dump(banco_login, f)

class JogosJSON:
    def ler(caminho):
        with open(caminho, 'r') as f:
            return json.load(f)

    def escrever(jogo: dict, caminho):
        #Caso a escolha seja acrescentar um jogo ao banco de dados
        banco_jogos = UsuarioJSON.ler(caminho)
        with open(caminho, 'w') as f:
            banco_jogos['jogos'].append(jogo.dict(include={"nome", "console", "popularidade", "categoria", "data"}))
            print(banco_jogos)
            return json.dump(banco_jogos, f)
        
    def deletar(jogo: dict, caminho):
        #Caso a escolha seja deletar um jogo do banco de dados
        banco_jogos = UsuarioJSON.ler(caminho)
        banco_jogos['jogos'].remove(jogo)
        with open(caminho, 'w') as f:
            print(banco_jogos)
            return json.dump(banco_jogos, f)

class UsuarioJSON:
    def ler(caminho):
        with open(caminho, 'r') as f:
            return json.load(f)

    def escrever(usuario: dict, caminho):
        #Caso a escolha seja acrescentar um usuário ao banco de dados
        banco_user = UsuarioJSON.ler(caminho)
        with open(caminho, 'w') as f:
            banco_user['usuarios'].append(usuario.dict(include={"nome", "email", "data", "jogos", "nivel", "pontos"}))
            print(banco_user)
            return json.dump(banco_user, f)
        
    def deletar(usuario: dict, caminho):
        #Caso a escolha seja deletar um usuário do banco de dados
        banco_user = UsuarioJSON.ler(caminho)
        banco_user['usuarios'].remove(usuario)
        with open(caminho, 'w') as f:
            print(banco_user)
            return json.dump(banco_user, f)

    def atualizar(usuario: dict, jogo, caminho):
        banco_user = UsuarioJSON.ler(caminho)
        banco_user['usuarios'].remove(usuario)
        usuario["jogos"].append(jogo)
        with open(caminho, 'w') as f:
            banco_user['usuarios'].append(usuario)
            print(banco_user)
            return json.dump(banco_user, f)
