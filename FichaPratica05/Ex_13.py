import math

def quadrado(comprimento):
    return comprimento * comprimento

def retangular(comprimento, largura):
    return comprimento * largura

def triangular(base, altura):
    return base * altura / 2

def circular(raio):
    return math.pi * (raio ** 2)


print("\nCálculo do Preço dos Terrenos (m/2)")
print("1. Terreno com forma Quadrada")
print("2. Terreno com forma Retângular")
print("3. Terreno com forma Triangular")
print("4. Terreno com forma Circular\n")

forma_terreno = int(input("Qual a forma do seu terreno?\n"))

match forma_terreno:
    case 1:
        comprimento = int(input("Introduza o comprimento: "))
        area = quadrado(comprimento)
        print(area)

    case 2:
        comprimento = int(input("Introduza o comprimento: "))
        largura = int(input("Introduza a largura: "))
        area = retangular(comprimento, largura)
        print(area)

    case 3:
        base = int(input("Introduza a base: "))
        altura = int(input("Introduza a altura: "))
        area = triangular(base, altura)
        print(area)

    case 4:
        raio = int(input("Introduza o raio: "))
        area = circular(raio)
        print(area)
    case _:
        print("Forma de Terreno Inválida!")


preco_terreno = int(input("Indique o preço do terreno: "))

print("\n###Tipologia do Terreno###")
print("1. URBANO")
print("2. URBANIZAVEL")
print("3. RUSTICOS\n")
tipologia = int(input("Indique a tipologia do terreno"))

preco_m2 = preco_terreno / area
print(preco_m2)

match tipologia:
    case 1:
        if 450 <= preco_m2 <= 750:
            print("Valor está dentro do valor do mercado.")
        else:
            print("Valor não está dentro do valor do mercado.")
            if preco_m2 < 450:
                print("Valor está abaixo do valor do mercado.")
                print("Valor excedente abaixo: ", 450 - preco_m2, "€/m2")
            elif preco_m2 > 750:
                print("Valor está acima do valor do mercado.")
                print("Valor excedente acima: ", preco_m2 - 750, "€/m2")

    case 2:
        if 150 <= preco_m2 <= 500:
            print("Valor está dentro do valor do mercado.")
        else:
            print("Valor não está dentro do valor do mercado.")
            if preco_m2 < 150:
                print("Valor está abaixo do valor do mercado.")
                print("Valor excedente abaixo: ", 150 - preco_m2, "€/m2")
            elif preco_m2 > 500:
                print("Valor está acima do valor do mercado.")
                print("Valor excedente acima: ", preco_m2 - 500, "€/m2")

    case 3:
        if 30 <= preco_m2 <= 60:
            print("Valor está dentro do valor do mercado.")
        else:
            print("Valor não está dentro do valor do mercado.")
            if preco_m2 < 30:
                print("Valor está abaixo do valor do mercado.")
                print("Valor excedente abaixo: ", 30 - preco_m2, "€/m2")
            elif preco_m2 > 60:
                print("Valor está acima do valor do mercado.")
                print("Valor excedente acima: ", preco_m2 - 60, "€/m2")

    case _:
        print("Tipologia do terreno Inválido!")