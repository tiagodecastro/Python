numero = []
encontrado = False

for i in range (0,10):
    num = int(input(f"Introduza um número no Array[{i}]:"))
    numero.append(num)


pesquisa = int(input("Número a pesquisar: "))
for i in range (0, 10):
    if numero[i] == pesquisa:
        print(f"{pesquisa} existe na Array[{i}]")
        encontrado = True

if not encontrado:
    print(f"{pesquisa} não existe na Array")