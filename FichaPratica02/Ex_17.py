# Ler Saldo Médio
print("Introduza o saldo médio: ")
saldomedio = float(input())

# Calcular Valor do Crédito
if saldomedio <= 2000:
    print("Nenhum crédito atribuído!")
elif 2000 < saldomedio <= 4000:
    print(f"Saldo Médio: {saldomedio} e Valor de Crédito: {saldomedio * 0.2}")
elif 4000 < saldomedio <= 6000:
    print(f"Saldo Médio: {saldomedio} e Valor de Crédito: {saldomedio * 0.3}")
elif saldomedio > 6000:
    print(f"Saldo Médio: {saldomedio} e Valor de Crédito: {saldomedio * 0.4}")