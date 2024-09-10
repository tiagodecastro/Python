# Ler Horas
print("Introduza as horas: ")
horas = int(input())

# Ler Minutos
print("Introduza os minutos: ")
minutos = int(input())

# Apresentar Horas em Formato AM e PM
if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
    print("Erro: Hora ou minutos inválidos!")
else:
# Verificar se é AM ou PM
    if horas <= 11:
        print(f"{horas}:{minutos} AM")
    elif horas >= 12:
        horas -= 12
        print(f"{horas}:{minutos} PM")