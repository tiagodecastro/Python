numero=[]

for i in range(0,10):
    num = int(input(f"Insira o número {i}: "))
    numero.append(num)

numero.sort()  # Ordena a lista
maior = numero[-1]  # O último elemento da lista ordenada é o maior

print(f"O maior número é: {maior}")