lista = ["banana", "banana", "banana", "banana", "banana", "banana", "pizza", "pizza", "pizza", "pizza", "pizza", "pizza"]

contador={}

for i in lista:
    if i in contador:
        contador[i] += 1

    else:
        contador[i] = 1

print(contador)
for lista, a in contador.items():
    print(f"{lista} : {a}")