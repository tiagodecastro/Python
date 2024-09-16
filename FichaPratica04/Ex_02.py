while True:
    # Menu
    print("1. Criar")
    print("2. Atualizar")
    print("3. Eliminar")
    print("4. Sair")

    opcao = input("Escolha uma opção 1-4: ")

    if opcao == '1':
        print("Opção Escolhida: 1. Criar")
    elif opcao == '2':
        print("Opção Escolhida: 2. Atualizar")
    elif opcao == '3':
        print("Opção Escolhida: 3. Eliminar")
    elif opcao == '4':
        print("Opção Escolhida: 4. Sair. Programa terminado")
        break
    else:
        print("Opção Inválida, tente novamente: ")