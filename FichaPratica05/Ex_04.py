def calculararearetangulo(base, altura):
    return base * altura

base = int(input("Introduza a base do retângulo: "))
altura = int(input("Introduza a altura do retângulo: "))

area = calculararearetangulo(base, altura)
print("A área do retângulo é:", area)