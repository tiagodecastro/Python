num = 0
anterior = 0
crescente = None
print("Quantos números deseja inserir: ")
quant = int(input())
ciclo = 1

while ciclo <= quant :
    print("Introduza um número: ")
    num = int(input())

    if anterior is not None:
        if num < anterior:
            crescente = False
    if anterior is not None and crescente != False:
        if num > anterior:
            crescente = True

    anterior = num
    ciclo += 1

if crescente:
    print("Sequência: Crescente")
else:
    print("Sequência: Não Crescente")
