# Ler número múltiplo de 5
print("Introduza um número múltiplo de 5: ")
numero = int(input())

# Decompor Valor
notas200 = numero // 200
numero %= 200
print(f"{notas200} notas de 200")

notas100 = numero // 100
numero %= 100
print(f"{notas100} notas de 100")

notas50 = numero // 50
numero %= 50
print(f"{notas50} notas de 50")

notas20 = numero // 20
numero %= 20
print(f"{notas20} notas de 20")

notas10 = numero // 10
numero %= 10
print(f"{notas10} notas de 10")

notas5 = numero // 5
numero %= 5
print(f"{notas5} notas de 5")