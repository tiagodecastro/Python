def imprimirtabuada(numero):
    i = 0
    while i < 11 :
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")
        i += 1

numero = int(input("Introduza um número para a tabuada: "))

imprimirtabuada(numero)