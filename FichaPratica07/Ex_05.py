formandos = {
    "Joao":[8,7,9],
    "Maria":[16,19,18],
    "Ana":[19,18,20]
}

pesquisa = input("Introduza o nome do formando: ")

if pesquisa in formandos:
    media = sum(formandos[pesquisa]) / len(formandos[pesquisa])
    print(f"Média de {pesquisa}: {media}")
else:
    print("Formando não encontrado")