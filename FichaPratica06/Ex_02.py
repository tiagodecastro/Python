comissao=[]
totalanual = 0

for i in range(0,12):
    preco = int(input(f"Insira a Comissão mensal do mês {i + 1}: "))
    comissao.append(preco)
    totalanual += preco

print(f"Total anual: {totalanual}")