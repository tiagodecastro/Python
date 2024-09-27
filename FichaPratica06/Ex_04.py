numero=[]

for i in range(0,10):
    num = int(input(f"Insira o número {i}: "))
    numero.append(num)

numero.sort()  # Ordena a lista
menor = numero[0]  # O último elemento da lista ordenada é o maior

print(f"O menor número é: {menor}")