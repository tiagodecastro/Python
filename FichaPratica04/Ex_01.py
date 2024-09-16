while True:
    # Ler num1
    print("Introduza um valor: ")
    num1 = int(input())

    # Ler num2
    print("Introduza um valor: ")
    num2 = int(input())

    # Ler operador
    print("Introduza um operador: ")
    operador = str(input())

    if operador == '+':
        calculo = num1 + num2
    elif operador == '-':
        calculo = num1 - num2
    elif operador == '*':
        calculo = num1 * num2
    elif operador == '/':
        calculo = num1 / num2

    print(calculo)
    print("Deseja continuar? (S/N)")
    continuar = str(input())

    if continuar == 'N' or continuar == 'n':
        print("Programa terminado!")
        break