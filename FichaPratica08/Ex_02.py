listaprodutos=[]

opcao = 0

if input("Username: ")=='gestor' and input("Password: ")=='pass123':
    while opcao != 8:

        print("1. Adicionar novo produto ao stock")
        print("2. Remover um produto do stock")
        print("3. Editar a quantidade ou o preço de um produto, dado o seu nome")
        print("4. Visualizar todos os produtos de uma estante dado o ID da estante")
        print("5. Calcular o valor total de uma estante")
        print("6. Calcular o valor total da loja")
        print("7. Identificar estantes mistas")
        print("8. Sair")

        opcao = int(input("Escolha a opção: "))


        match opcao:
            case 1:
                dicionario = {
                    "produto":input("Introduza o nome do produto: "),
                    "categoria":input("Introduza a categoria do produto: "),
                    "quantidade":int(input("Introduza a quantidade do produto: ")),
                    "preço":float(input("Introduza o preço: "))
                }
                listaprodutos.append(dicionario)
            case 2:
                remover = input("Introduza o nome do produto: ")
                for i in range(len(listaprodutos)):
                    if remover == listaprodutos[i]["produto"]:
                        print(listaprodutos[i])
            case 7:
                pass
            case 8:
                pass
            case _:
                print("Opção Inválida!")