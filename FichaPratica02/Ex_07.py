# Ler um número
print("Introduza um número: ")
num1 = int(input())

# Verificar se é par ou ímpar
verificarnum = num1 % 2

if verificarnum == 0:
    print(f"O número {num1} é par.")

elif verificarnum != 0:
    print(f"O número {num1} é ímpar.")

else:
    print("Número inválido!")