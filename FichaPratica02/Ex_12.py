# Ler Opção Menu
print(f"Escolha a sua opção:")
print("1 - Criar")
print("2 - Atualizar")
print("3 - Eliminar")
print("4 - Sair")
opcao = str(input())

# Apresentar Opção selecionada
if opcao == '1':
    print("Opção Selecionada: 1 - Criar")

elif opcao == '2':
    print("Opção Selecionada: 2 - Atualizar")

elif opcao == '3':
    print("Opção Selecionada: 3 - Eliminar")

elif opcao == '4':
    exit

else:
    print("Opção Inválida!")