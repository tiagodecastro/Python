# Ler num1
print("Introduza o primeiro número: ")
num1 = int(input())

# Ler num2
print("Introduza o segundo número: ")
num2 = int(input())

# Verificar maior e menor número
if num1 > num2:
    print(f"{num1} e {num2}")
elif num2 > num1:
    print(f"{num2} e {num1}")
elif num1 == num2:
    print(f"{num1} e {num2} são iguais")