import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO cliente (nome, email) VALUES (?,?)',('Teste 3', 'teste3@gmail.com'))
    # cursor.execute('INSERT INTO cliente (id, nome, email) VALUES (?,?,?)',(4,'Teste 4', 'teste4@gmail.com'))
    cursor.execute('DELETE FROM cliente WHERE id = 9,8;')
    conexao.commit()

except Exception as exc:
    print(f'Ops! um erro ocorreu! {exc}')
    conexao.rollback()




