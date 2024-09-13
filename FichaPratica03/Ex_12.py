print("Introduza o valor de ínício: ")
inicio = int(input())

print("Introduza o valor de fim: ")
fim = int(input())

while inicio <= fim:
    multiplo = inicio % 5
    if multiplo == 0:
        print("Números múltiplos de 5: ", inicio)
    inicio += 1