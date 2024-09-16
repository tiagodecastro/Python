tentativas = 0

# Pedir número de 1 a 100
escolhernum = int(input("Introduza um número de 1 a 100: "))

while True:
    # Pedir para adivinhar número
    acertarnum = int(input("Tente adivinhar o número escolhido: "))

    tentativas += 1

    # Verificar se numero se acertou no número
    if escolhernum < acertarnum:
        print("O número que escolheu é maior que o valor introduzido")
    if escolhernum > acertarnum:
        print("O número que escolheu é menor que o valor introduzido")
    if escolhernum == acertarnum:
        print("Parabéns! Acertou no número!")
        print(f"Tentou {tentativas} vezes!")
        break