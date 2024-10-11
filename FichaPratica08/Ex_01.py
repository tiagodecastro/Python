listaFuncionarios = []

opcao = 0

while opcao != 8:
    print("1. Adicionar Novos Funcionários")
    print("2. Remover Funcionários")
    print("3. Editar Dados de um Funcionário")
    print("4. Listar todos os Funcionários")
    print("5. Pesquisar ID de Funcionário")
    print("6. Pagamento em Salários Mensal")
    print("7. Cálculo de Aumentos")
    print("8. Sair")

    opcao = int(input("Escolha a sua opção: "))

    match opcao:
        case 1:
            id = input("ID: ")
            nome = input("Nome: ")
            anoNascimento = input("Ano de Nascimento:" )
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))

            funcionarios = {
                "ID":id,
                "nome": nome,
                "anoNascimento": anoNascimento,
                "cargo": cargo,
                "salário": salario
            }
            listaFuncionarios.append(funcionarios)

        case 2:
            remover = input("Introduza o ID do Funcionário a remover: ")

            for i in range(len(listaFuncionarios)):
                if listaFuncionarios[i]["ID"] == remover:
                    listaFuncionarios.pop(i)
                    print(f"Funcionário {remover} removido.")
                    break
            else:
                print(f"Funcionário {remover} não encontrado")

        case 3:
            pesquisa = input("Introduza o ID do Funcionário: ")

            for i in range(len(listaFuncionarios)):
                if listaFuncionarios[i]["ID"] == pesquisa:
                    cargo = input("Introduza o novo cargo: ")
                    salario = float(input("Introduza o novo salário: "))
                    listaFuncionarios[i]["cargo"] = cargo
                    listaFuncionarios[i]["salário"] = salario
            else:
                print(f"Funcionário {pesquisa} não encontrado")
        case 4:
            for i in range(len(listaFuncionarios)):
                print("\n", listaFuncionarios[i])
        case 5:
            pesquisa = (input("Introduza o ID do Funcionário: "))

            for i in range(len(listaFuncionarios)):
                if listaFuncionarios[i]["ID"] == pesquisa:
                    print(listaFuncionarios[i])
        case 6:
            soma = 0
            for i in range(len(listaFuncionarios)):
                soma += listaFuncionarios[i]["salário"]
            print(f"Soma: {soma}")
        case 7:
            aumento = int(input("Percentagem de Aumento: ")) / 100
            somatorio = 0
            for i in (range(len(listaFuncionarios))):
                somatorio += listaFuncionarios[i]["salário"]
            print("Pagaria:", somatorio + somatorio * aumento)

        case 8:
            print("A sair...")
        case _:
            print("Opção inválida!")
