from unittest.mock import Mock
import usuario

def cria_mock_conexao():
    # cria mock de conexão e cursor
    mock_conexao = Mock()
    mock_cursor = Mock()
    # retorna o mock do cursor ao chamar conexao.cursor()
    mock_conexao.cursor.return_value = mock_cursor
    return mock_conexao, mock_cursor

def test_cadastrar_usuario(monkeypatch):
    # mock de conexão e cursor
    mock_conexao, mock_cursor = cria_mock_conexao()
    monkeypatch.setattr('usuario.checar_conexao', lambda: mock_conexao)
    # cadastra novo usuário
    usuario.cadastrar_usuario('Alice', 30, 'alice@gmail.com')
    # verifica se a query foi executada corretamente
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO tb_usuarios (nome, idade, email) VALUES (%s, %s, %s)", 
        ('Alice', 30, 'alice@gmail.com')
    )
    # confirma commit e fechamento da conexão
    mock_conexao.commit.assert_called_once()
    mock_conexao.close.assert_called_once()

def test_listar_usuarios(monkeypatch, capsys):
    # mock de conexão e cursor
    mock_conexao, mock_cursor = cria_mock_conexao()
    # define retorno do fetchall
    mock_cursor.fetchall.return_value = [(1, 'Adélia', 22, 'adelia@gmail.com'), (2, 'Camille', 21, 'camille@gmail.com')]
    monkeypatch.setattr('usuario.checar_conexao', lambda: mock_conexao)
    # lista usuários
    usuario.listar_usuarios()
    # captura a saída do print
    capturado = capsys.readouterr().out
    # verifica se os usuários foram impressos corretamente
    assert "(1, 'Adélia', 22, 'adelia@gmail.com')" in capturado
    assert "(2, 'Camille', 21, 'camille@gmail.com')" in capturado
    # fecha a conexão
    mock_conexao.close.assert_called_once()

def test_atualizar_usuario(monkeypatch):
    # mock de conexão e cursor
    mock_conexao, mock_cursor = cria_mock_conexao()
    monkeypatch.setattr('usuario.checar_conexao', lambda: mock_conexao)
    # atualiza nome do usuário com id = 1
    usuario.atualizar_usuario(1, nome='Adélia Atualizado')
    # define a query e parâmetros esperados
    query_esperada = "UPDATE tb_usuarios SET nome = %s WHERE id = %s"
    parametros_esperados = ('Adélia Atualizado', 1)
    # verifica se a query foi executada corretamente
    mock_cursor.execute.assert_called_once_with(query_esperada, parametros_esperados)
    # commit e fechamento da conexão
    mock_conexao.commit.assert_called_once()
    mock_conexao.close.assert_called_once()

def test_deletar_usuario(monkeypatch):
    # mock de conexão e cursor
    mock_conexao, mock_cursor = cria_mock_conexao()
    monkeypatch.setattr('usuario.checar_conexao', lambda: mock_conexao)
    # deleta usuário com id = 3
    usuario.deletar_usuario(3)
    # verifica se a query foi executada corretamente
    mock_cursor.execute.assert_called_once_with("DELETE FROM tb_usuarios WHERE id = %s", (3,))
    # commit e fechamento da conexão
    mock_conexao.commit.assert_called_once()
    mock_conexao.close.assert_called_once()