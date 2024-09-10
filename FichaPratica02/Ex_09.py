# Ler num1
print("Introduza um número: ")
num1 = float(input())

# Ler num2
print("Introduza um número: ")
num2 = float(input())

# Ler num3
print("Introduza um número: ")
num3 = float(input())

# Mostrar o menor dos 3 números
if num1 < num2 and num1 < num3:
    print(f"{num1} é o número mais baixo.")
elif num2 < num1 and num2 < num3:
    print(f"{num2} é o número mais baixo.")
elif num3 < num1 and num3 < num2:
    print(f"{num2} é o número mais baixo.")