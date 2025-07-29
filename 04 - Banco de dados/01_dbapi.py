import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )


conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(
        "INSERT INTO cliente (nome, email) VALUES (?, ?);",
        data,
    )


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE cliente SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


atualizar_registro(conexao, cursor, "Felipe Prates", "fdsprates@gmail.com", 1)
atualizar_registro(conexao, cursor, "Joice Prates", "joice@gmail.com", 2)


def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM cliente WHERE id=?;", data)
    conexao.commit()


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO cliente(nome, email) VALUES (?, ?)", dados)
    conexao.commit()


def recuperar_clientes(cursor, id):
    cursor.execute("SELECT * FROM cliente WHERE id=?", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM cliente ORDER BY nome;")


cliente = listar_clientes(cursor)
for cliente in cliente:
    print(dict(cliente))

cliente = recuperar_clientes(cursor, 2)
print(dict(cliente))

print(f"Seja bem vindo ao sitema {cliente['nome']}")


# Lista de dados (nome, email) para inserção em massa
# dados = [
#     ("Felipe", "fdsp@gmail.com"),
#     ("Joice", "joi@gmail.com"),
#     ("Lucas", "lu@gmail.com"),
#     ("Angela", "ange@gmail.com"),
#     ("Fernando", "fer@gmail.com"),
# ]

# # Insere todos os dados da lista no banco de dados
# inserir_muitos(conexao, cursor, dados)
