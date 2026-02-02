import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

while True:
    print("\nGERADOR DE SENHAS")
    print("1 - Gerar senhas")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        qtd = int(input("Quantas senhas deseja gerar? "))
        tamanho = int(input("Tamanho da senha (4 a 20): "))

        if not (4 <= tamanho <= 20):
            print("Tamanho inválido. Escolha um valor entre 4 e 20.")
        else:
            senhas = set()
            while len(senhas) < qtd:
                senhas.add(gerar_senha(tamanho))

            print("\nSenhas geradas:")
            for i, senha in enumerate(senhas, 1):
                print(f"{i}: {senha}")

    elif opcao == "2":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
