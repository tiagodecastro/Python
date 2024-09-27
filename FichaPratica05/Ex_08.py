
char = input("Introduza um caracter: ")
linhas = int(input("Introduza um número de linhas: "))
colunas = int(input("Introduza um número de colunas: "))
ciclo = 1
char_func = ' ' * colunas
while ciclo <= colunas:
    if ciclo == (colunas) or ciclo == 1:
        print(char * colunas)
    else:
        print(char,char_func,char)
    ciclo += 1