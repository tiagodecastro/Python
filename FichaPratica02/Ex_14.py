# Ler num1
print("Introduza um número: ")
num1 = int(input())

# Ler num2
print("Introduza outro número: ")
num2 = int(input())

# Ler num3
print("Introduza outro número: ")
num3 = int(input())

# Colocar por ordem crescente
if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2

print("Números por ordem crescente: ", num1, num2, num3)