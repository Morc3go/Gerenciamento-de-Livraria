from src.db import conectar_bd

def adicionar_livro(titulo, autor, ano_publicacao, preco):
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO livros (titulo, autor, ano_publicacao, preco) 
                          VALUES (?, ?, ?, ?)''', (titulo, autor, ano_publicacao, preco))
        conn.commit()
        print("Livro adicionado com sucesso!")

def exibir_livros():
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        for livro in livros:
            print(livro)

def atualizar_preco(id_livro, novo_preco):
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, id_livro))
        conn.commit()
        print("Preço atualizado com sucesso!")

def remover_livro(id_livro):
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
        conn.commit()
        print("Livro removido com sucesso!")

def buscar_por_autor(autor):
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros WHERE autor = ?", (autor,))
        livros = cursor.fetchall()
        for livro in livros:
            print(livro)
