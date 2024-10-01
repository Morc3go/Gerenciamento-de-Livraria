from pathlib import Path
import sqlite3

db_dir = Path("meu_sistema_livraria/data")
db_path = db_dir / "livraria.db"
db_dir.mkdir(parents=True, exist_ok=True)

def conectar_bd():
    return sqlite3.connect(db_path)

def criar_tabela():
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            autor TEXT NOT NULL,
                            ano_publicacao INTEGER NOT NULL,
                            preco REAL NOT NULL)''')
        conn.commit()

criar_tabela()
