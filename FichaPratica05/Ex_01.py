


def lervalorpositivo():
    while True:
        valor = int(input("Introduza um número:"))
        if valor > 0:
            return valor
        else:
            print("Introduza um valor positivo.")

def asteriscos(valor):
    print("*" * valor)

# valor = lervalorpositivo()
asteriscos(lervalorpositivo())