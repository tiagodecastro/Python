qt = 0
calculo = 0
n = 0

while n != -1:
    print("Introduza um número: ")
    n = int(input())
    qt += 1
    calculo += n

media = calculo / qt
print(f"Média é: {media:.2f}")