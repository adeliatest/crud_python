import mysql.connector
from config import DB_CONFIG

def checar_conexao():
    try:
        # verifica a conexão com o banco de dados
        conexao = mysql.connector.connect(**DB_CONFIG)
        if conexao.is_connected():
            print("Conexão bem sucedida!")
        return conexao
    except mysql.connector.Error as err:
        # informa o erro caso a conexão falhep
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
    
checar_conexao()