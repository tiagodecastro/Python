from FichaPratica05.Ex_06 import parouimpar, positivo, primo, perfeito, triangular

num = int(input("Insira um número: "))
opcao = 0

while opcao != 7 :
    print("### Análise de Número ###\n")
    print("1. Par ou Ímpar")
    print("2. Positivo ou Negativo")
    print("3. Primo ou Não Primo")
    print("4. Perfeito ou Não Perfeito")
    print("5. Triangular ou Não Triangular")
    print("6. Trocar de Número")
    print("7. Sair")

    opcao = int(input("\nIntroduza uma opção:\n"))

    match (opcao):
        case 1:
            if parouimpar(num):
                print("O número é par.\n")
            else:
                print("O número é impar.\n")
        case 2:
            if positivo(num):
                print("O número é positivo.\n")
            else:
                print("O número é negativo.\n")

        case 3:
            if primo(num):
                print("O número é primo.\n")
            else:
                print("O número não é primo.\n")

        case 4:
            if perfeito(num):
                print("O número é perfeito.\n")
            else:
                print("O número não é perfeito.\n")
        case 5:
            if triangular(num):
                print("O número é triângular.\n")
            else:
                print("O número não é triângular.\n")

        case 6:
            num = int(input("Insira um número: \n"))
