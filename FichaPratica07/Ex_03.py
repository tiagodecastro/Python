listaContactos=[]

contacto = {
    "nome": "Tiago Castro",
    "telemovel": "919999999",
    "morada" : "Porto"
}

listaContactos.append(contacto)

opcao = 0

while opcao != 4 :
    print("****** Lista de Contactos *****")
    print("1. Adicionar Novo Contacto")
    print("2. Consultar Lista de Contactos")
    print("3. Pesquisar um Contacto")
    print("4. Sair")
    opcao=int(input("Opção desejada:"))

    match opcao:
        case 1:
            print("\nAdicionar Novo Contacto")
            nome = input("Nome: ")
            telemovel = input("Telemovel: ")
            morada = input("Morada: ")

            novoContacto = {
                "nome": nome,
                "telemovel": telemovel,
                "morada": morada
            }

            print("Estes dados estão corretos?")
            print(novoContacto)

            confirma = input("Deseja continuar? (S/N)").upper()

            if confirma == 'S':
                listaContactos.append(novoContacto)
                print("Contacto inserido")
            else:
                print("Contacto não inserido")

        case 2:
            print("\nConsultar Lista de Contactos")
            for contacto in listaContactos:
                print(contacto)

        case 3:
            print("\nPesquisar um Contacto")
            pesquisa = input("Introduza o termo a pesquisar")
            for contacto in listaContactos:
                if pesquisa in contacto['nome'] or pesquisa in contacto['telemovel'] or pesquisa in contacto['morada']:
                    print("Nome: ", contacto['nome'])
                    print("Telemóvel :", contacto['telemovel'])
                    print("Morada :", contacto['morada'], "\n")

                else:
                    print("Contacto não encontrado")

        case 4:
            print("\nA sair...")

        case _:
            print("Opção inválida, tente novamente")