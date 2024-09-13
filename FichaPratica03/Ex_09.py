print("Introduza um número inteiro: ")
n = int(input())

ciclo = 2
while ciclo <= n:
    par = ciclo % 2
    if par == 0:
        print(ciclo)
    ciclo += 1