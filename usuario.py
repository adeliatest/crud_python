from database import checar_conexao

def cadastrar_usuario(nome,idade, email):
    # utiliza a função checar_conexao do database.py
    conexao = checar_conexao()
    cursor = conexao.cursor()
    # executa a query
    cursor.execute("INSERT INTO tb_usuarios (nome, idade, email) VALUES (%s, %s, %s)", (nome, idade, email))
    # commit e fecha a conexão
    conexao.commit()
    print(f"Usuário {nome} cadastrado com sucesso!")
    conexao.close()

def listar_usuarios():
    # utiliza a função checar_conexao do database.py
    conexao = checar_conexao()
    cursor = conexao.cursor()
    # executa a query
    cursor.execute("SELECT * FROM tb_usuarios")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    # fecha a conexão
    conexao.close()

def atualizar_usuario(user_id, nome=None, idade=None, email=None):
    # utiliza a função checar_conexao do database.py
    conexao = checar_conexao()
    cursor = conexao.cursor()
    # monta a query de forma dinâmica
    campos = []
    valores = []
    # atualiza apenas os campos que foram fornecidos
    if nome:
        campos.append("nome = %s")
        valores.append(nome)
    if idade:
        campos.append("idade = %s")
        valores.append(idade)
    if email:
        campos.append("email = %s")
        valores.append(email)
    valores.append(user_id)
    sql = f"UPDATE tb_usuarios SET {', '.join(campos)} WHERE id = %s"
    cursor.execute(sql, tuple(valores))
    # commit e fecha a conexão
    conexao.commit()
    print(f"Usuário com ID {user_id} atualizado com sucesso!")
    conexao.close()

def deletar_usuario(user_id):
    # utiliza a função checar_conexao do database.py
    conexao = checar_conexao()
    cursor = conexao.cursor()
    # executa a query
    cursor.execute("DELETE FROM tb_usuarios WHERE id = %s", (user_id,))
    # commit e fecha a conexão
    conexao.commit()
    print(f"Usuário com ID {user_id} deletado com sucesso!")
    conexao.close()

