numero = []
maior = 0

for i in range (0,10):
    num = int(input("Introduza um valor: "))
    numero.append(num)

    if (num % 2) == 0 and maior < num:
        maior = num

if num != 0:
    print("O maior número par é: ", maior)

else:
    print("Não inseriu um número par")