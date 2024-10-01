from src.livros import adicionar_livro, exibir_livros, atualizar_preco, remover_livro, buscar_por_autor
from src.arquivos import exportar_para_csv, importar_de_csv
from src.backup import criar_backup, limpar_backups_antigos


def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo livro")
        print("2. Exibir todos os livros")
        print("3. Atualizar preço de um livro")
        print("4. Remover um livro")
        print("5. Buscar livros por autor")
        print("6. Exportar dados para CSV")
        print("7. Importar dados de CSV")
        print("8. Fazer backup do banco de dados")
        print("9. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de Publicação: "))
            preco = float(input("Preço: "))
            adicionar_livro(titulo, autor, ano, preco)
            criar_backup()
        elif escolha == '2':
            exibir_livros()
        elif escolha == '3':
            id_livro = int(input("ID do Livro: "))
            novo_preco = float(input("Novo Preço: "))
            atualizar_preco(id_livro, novo_preco)
            criar_backup()
        elif escolha == '4':
            id_livro = int(input("ID do Livro: "))
            remover_livro(id_livro)
            criar_backup()
        elif escolha == '5':
            autor = input("Autor: ")
            buscar_por_autor(autor)
        elif escolha == '6':
            exportar_para_csv()
        elif escolha == '7':
            csv_file = input("Caminho do arquivo CSV: ")
            importar_de_csv(csv_file)
        elif escolha == '8':
            criar_backup()
            limpar_backups_antigos()
        elif escolha == '9':
            break
        else:
            print("Opção inválida. Tente novamente.")
