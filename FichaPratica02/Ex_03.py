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




'''# Declarar variáveis para calcular Taxa Marginal
salariomarginal10k = 3000
salariomarginal15k = (20000 - 15000) * 0.3
salariomarginal20k = (25000 - 20000) * 0.35
salariomarginal25k = (salarioanual - 25000) * 0.4

# Cáculo Real do Mundo Real da Taxa Marginal a ser Paga!!!!
if salarioanual <= 15000:
    print("Paga taxa de 20%: ", salarioanual * 0.2)

elif 15000 < salarioanual <= 20000:
    print("Paga Taxa Marginal:", salariomarginal10k + salariomarginal15k)
    print("Paga Taxa de 30%:", salarioanual * 0.3)

elif 20000 < salarioanual <= 25000:
    salariomarginal = salarioanual - 20000
    print("Paga Taxa Marginal: ", salariomarginal10k + salariomarginal15k + salariomarginal20k)
    print("Paga Taxa de 35%:", salarioanual * 0.35)

elif salarioanual > 25000:
    salariomarginal = salarioanual - 25000
    print("Paga Taxa Marginal: ", salariomarginal10k + salariomarginal15k + salariomarginal20k + salariomarginal25k)
    print("Paga Taxa de 40%:", salarioanual * 0.4)'''