import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")

cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150), telefone VACHAR(20))"
    )


conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(
        "INSERT INTO cliente (nome, email) VALUES (?,?,?);",
        data,
    )


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE cliente SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()

atualizar_registro(conexao, cursor, "Felipe Prates", "fdsprates@gmail.com", 1)
atualizar_registro(conexao, cursor, "Joice Prates", "joice@gmail.com", 2)


def deletar_registro(conexao, cursor, id):
    data = ((id),)
    cursor.execute("DELETE FROM cliente WHERE id=?;", data)
    conexao.commit()


deletar_registro(conexao, cursor, 1)
