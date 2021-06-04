import json, usuario

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

    def escrever(user: dict, caminho):
        #Caso a escolha seja acrescentar um usuário ao banco de dados
        banco_user = UsuarioJSON.ler(caminho)
        with open(caminho, 'w') as f:
            banco_user['usuarios'].append(user.dict(include={"nome", "email", "data", "jogos", "nivel", "pontos"}))
            print(banco_user)
            return json.dump(banco_user, f)
        
    def deletar(user: dict, caminho):
        #Caso a escolha seja deletar um usuário do banco de dados
        banco_user = UsuarioJSON.ler(caminho)
        banco_user['usuarios'].remove(user)
        with open(caminho, 'w') as f:
            print(banco_user)
            return json.dump(banco_user, f)

    def atualizar(user: dict, caminho):
        #Lê o banco de dados, recupera o usuário a ser atualizado com o email e logo após exlcui esse registro antigo do usuário
        #Após excluir o registro ele lê o banco e adicionar novamente com o usuário com informações novas
        banco_user = UsuarioJSON.ler(caminho)
        antigo = usuario.retornar_usuario(user["email"])
        banco_user['usuarios'].remove(antigo)
        with open(caminho, 'w') as f:
            banco_user['usuarios'].append(user)
            print(banco_user)
            return json.dump(banco_user, f)
