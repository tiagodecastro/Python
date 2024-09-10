# Ler Saldo da Conta Bancária
print("Introduza o saldo da conta bancária: ")
saldobancario = float(input())

# Ler Valor a Creditar/Debitar
print("Quer Creditar ou Debitar?")
operacao = str(input())

# Detetar se operação é para Debitar ou Creditar
if operacao == 'debitar' or operacao == 'Debitar':
    print("Introduza o valor a debitar: ")
    debito = float(input())
    # Operação Válida
    if saldobancario >= debito:
        print("Operação válida! Saldo: ", saldobancario - debito)
    # Operação Inválida
    elif saldobancario < debito:
        print("Operação inválida! Saldo insuficiente!")

elif operacao == 'Creditar' or operacao == 'creditar':
    print("Introduza o valor a creditar: "),
    credito = float(input())
    print("Operação válida! Saldo: ", saldobancario + credito)