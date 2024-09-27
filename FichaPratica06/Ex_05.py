numero = [ ]
num = 0
ciclo = 0

while True :
    num = int(input("Introduza um número: "))
    if num >= 0:
        numero.append(num)
    else:
        break
    ciclo += 1

media = sum(numero) / ciclo
print("Média é: ", media)
print("Foram lidos", ciclo, " números.")