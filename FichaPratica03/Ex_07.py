# Ler número
print("Introduza um número: ")
n = int(input())

# Declarar variável de ciclo
anterior = 1
seguinte = 1

# 5 números anteriores
while anterior <= 5:
    print (n - anterior)
    anterior += 1


# 5 números seguintes
while seguinte <= 5:
    print (n + seguinte)
    seguinte += 1