# Exercício 1 e 2 com menu de escolha

def exercicio_1():
    # Exemplo de lista de notas
    notas = [4.5, 3.6, 7.8, 8.9, 6.3, 5.4, 9.1, 2.4, 8.7, 6.8, 5.9, 7.0, 4.2, 6.5, 8.1, 9.5, 3.3, 7.4, 8.2, 9.0, 5.7, 4.8]

    # Exibindo os 12 primeiros registros
    print("Primeiros 12 registros:")
    print(notas[:12])

    # Exibindo os 6 últimos registros
    print("\nÚltimos 6 registros:")
    print(notas[-6:])

    # Exibindo o tamanho da massa de dados
    print("\nTamanho da massa de dados:", len(notas))


def exercicio_2():
    # Exemplo de lista de filmes com ID, nome e nota
    filmes = [
        {"ID": 30, "Nome": "Filme A", "Nota": 3.5},
        {"ID": 31, "Nome": "Filme B", "Nota": 2.0},
        {"ID": 32, "Nome": "Filme C", "Nota": 4.2},
        {"ID": 33, "Nome": "Filme D", "Nota": 5.0},
        {"ID": 34, "Nome": "Filme E", "Nota": 2.9},
    ]

    # Procurando pelo filme com ID=32
    filme_encontrado = None
    for filme in filmes:
        if filme["ID"] == 32:
            filme_encontrado = filme
            break

    # Verificando se o filme foi encontrado e se a nota é maior que 3
    if filme_encontrado:
        if filme_encontrado["Nota"] > 3:
            print(f"Filme: {filme_encontrado['Nome']} - Nota: {filme_encontrado['Nota']}")
            print("Este é um filme bom!")
        else:
            print(f"Filme: {filme_encontrado['Nome']} - Nota: {filme_encontrado['Nota']}")
            print("Este filme não é bom.")
    else:
        print("Filme com ID 32 não encontrado.")


def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Exercício 1: Análise de notas")
        print("2. Exercício 2: Análise de filme com ID=32")
        print("3. Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            exercicio_1()
        elif opcao == "2":
            exercicio_2()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa o menu
menu()
