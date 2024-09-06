# Ler Salário Anual
print("Introduza o Salário Anual: ")
salarioanual = int(input())

# Cáculo de Taxa a pagar
if salarioanual <= 15000:
    print("Paga taxa de 20%: ", salarioanual * 0.2)

elif 15000 < salarioanual <= 20000:
    print("Paga taxa de 30%: ", salarioanual * 0.3)

elif 20000 < salarioanual <= 25000:
    print("Paga taxa de 35%: ", salarioanual * 0.35)

elif salarioanual > 25000:
    print("Paga taxa de 40%: ", salarioanual * 0.40)