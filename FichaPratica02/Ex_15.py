# Ler num1
print("Introduza um número: ")
num1 = int(input())

# Ler num2
print("Introduza outro número: ")
num2 = int(input())

# Ler num3
print("Introduza outro número: ")
num3 = int(input())

# Ler Opção ordem crescente ou decrescente
print("Escolha (C) para colocar em ordem crescente ou (D) por ordem decrescente?")
opcao = str(input())

# Colocar por ordem decrescente
if opcao == 'D' or opcao == 'd':
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num2 < num3:
        num2, num3 = num3, num2
    print("Números por ordem decrescente: ", num1, num2, num3)

# Colocar por ordem crescente
elif opcao == 'C' or opcao == 'c':
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2
    print("Números por ordem crescente: ", num1, num2, num3)

else:
    print("Opção incorreta!")