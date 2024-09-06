# Ler Música 1
print("Introduza os minutos da música 1: ")
musicaminutos1 = int(input())
print("Introduza os segundos da música 1: ")
musicasegundos1 = int(input())

# Ler Música2
print("Introduza os minutos da música 2: ")
musicaminutos2 = int(input())
print("Introduza os segundos da música 2: ")
musicasegundos2 = int(input())

# Ler Música3
print("Introduza os minutos da música 3: ")
musicaminutos3 = int(input())
print("Introduza os segundos da música 3: ")
musicasegundos3 = int(input())

# Soma de Segundos, Minutos, Horas para uso
segundos = musicasegundos1 + musicasegundos2 + musicasegundos3
minutos = musicaminutos1 + musicaminutos2 + musicaminutos3

# Cálculo e Conversão de Segundos
contadorsegundos = segundos % 60
segundosemminutos = segundos // 60

# Cálculo e Conversão de Minutos
contadorminutos = minutos % 60 + segundosemminutos
minutosemhoras = minutos // 60

# Cálculo e Conversão de Horas
contadorhoras = minutosemhoras


print(f"Total do Álbum: {contadorhoras}h {contadorminutos}m {contadorsegundos}s")