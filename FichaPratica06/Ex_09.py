numero = []

for i in range (0,10):
    num = int(input(f"Introduza um número no Array[{i}]:"))
    numero.append(num)


pesquisa = int(input("Número a pesquisar: "))
for i in range (0, 10):
    encontrado = False
    if numero[i] == pesquisa:
        print(f"{pesquisa} existe na Array")
        encontrado = True
        break

if encontrado == False:
    print(f"{pesquisa} não existe na Array")