# Ler Valor1
print("Introduza o primeiro valor:")
valor1 = int(input())

# Ler Valor2
print("Introduza o segundo valor:")
valor2 = int(input())

# valor1, valor2 = valor2, valor1
# print("Valor1 = ", valor1)
# print("Valor2 = ", valor2)

# Solução Dificil!!!!!!!!!
valor1 = valor1 + valor2
valor2 = valor1 - valor2
valor1 = valor1 - valor2
print(f"{valor1} e {valor2}")