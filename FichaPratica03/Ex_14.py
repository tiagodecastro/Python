print("Introduza um número: ")
num = int(input())
fatorial = 1

while num != 0:

    fatorial *= num
    num -= 1

print("Fatorial:", fatorial)


# Desafio Não usar a Multiplicação
while num != 0:
    while num != 0:
        fatorial += num
        num -=1
    num -= 1

print("Fatorial Desafio:", fatorial)