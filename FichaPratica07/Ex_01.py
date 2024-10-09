# Dicionário de animais

animais = {
    "A": ["Andorinha", "Avestruz", "Alforreca"],
    "B": ["Baleia", "Borboleta", "Burro"],
    "C": ["Cachorro", "Cavalo", "Canguru"],
    "D": ["Dromedário", "Doninha", "Dragão-de-Komodo"],
    "E": ["Elefante", "Ema", "Esquilo"],
    "F": ["Falcão", "Foca", "Formiga"]
}

letra = input("Digite uma letra: ").upper()
if letra in animais:
    print(f"Animais com {letra}: ")
    for animal in animais[letra]:
        print(f" {animal}")

else:
    print("Não há animais com essa letra!")