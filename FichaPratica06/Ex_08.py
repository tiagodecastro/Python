numero = []

for i in range (0,10):
    num = int(input(f"Introduza um número no Array[{i}]:"))
    numero.append(num)

for i in range (10, 0, -1):
    print(f"{numero[i-1]}")