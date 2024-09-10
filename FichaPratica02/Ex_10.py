# Ler num1
print("Introduza o primeiro número: ")
num1 = float(input())

# Ler num2
print("Introduza o segundo número: ")
num2 = float(input())

# Escolher operação aritmética
print("Qual a operação aritmética que pretende? ")
operador = str(input())

if operador == '+':
    print("Soma: ", num1 + num2)
elif operador == '-':
    print("Substração: ", num1 - num2)
elif operador == '*':
    print("Multiplicação: ", num1 * num2)
elif operador == '/':
    print("Divisão: ", num1 / num2)
else:
    print("Erro! Operador inválido!")