import csv
from pathlib import Path
from src.db import conectar_bd

exports_dir = Path("meu_sistema_livraria/exports")
exports_dir.mkdir(parents=True, exist_ok=True)

def exportar_para_csv():
    with conectar_bd() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()

        csv_path = exports_dir / "livros_exportados.csv"
        with open(csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Título", "Autor", "Ano", "Preço"])
            writer.writerows(livros)

        print(f"Dados exportados para {csv_path}")

def importar_de_csv(csv_file):
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            with conectar_bd() as conn:
                cursor = conn.cursor()
                for row in reader:
                    cursor.execute(
                        "INSERT INTO livros (id, titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?, ?)", row)
                conn.commit()
            print(f"Dados importados de {csv_file}")
    except PermissionError:
        print(
            f"Permissão negada ao tentar acessar o arquivo: {csv_file}. Verifique se o arquivo está aberto ou se as permissões estão corretas.")
