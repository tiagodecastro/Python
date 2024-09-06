# Ler Salário Anual
print("Introduza o Salário Anual: ")
salarioanual = int(input())

# Cáculo de Taxa a pagar
if salarioanual <= 15000:
    print("Paga taxa de 20%: ", salarioanual * 0.2)
if salarioanual > 15000:
    print("Paga taxa de 30%: ", salarioanual * 0.3)