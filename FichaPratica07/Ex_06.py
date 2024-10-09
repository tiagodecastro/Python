lista_compras = {}

opcao = 0

while opcao != 3:
    print("Lista de Compras")
    print("1. Adicionar novo produto")
    print("2. Calcular o preço total")
    print("3. Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            produto = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))

            lista_compras[produto] = preco
            print(f"Adicionou o produto {produto} com o preço: {preco}")
        case 2:
            total = sum(lista_compras.values())
            print(f"Preço total: {total}")
        case 3:
            print("A sair...")
        case _:
            print("Opção inválida")