numero = []
crescente = True

for i in range (0,10):
    num = int(input("Introduza um número: "))
    numero.append(num)

    if numero[i] < numero[i - 1]:
        crescente = False
        break

if crescente == True:
    print("Ordem crescente")
else:
    print("Ordem não decrescente")