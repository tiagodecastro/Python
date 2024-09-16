num1 = int(input("Introduza um número: "))
ciclo = num1
divisor = 0

while ciclo > 0:
    if num1 % ciclo == 0:
        divisor += 1
    ciclo -= 1

if divisor == 2:
    print(f"O número {num1} é primo.")
else:
    print(f"O número {num1} não é primo.")
