# a) Função que determina se um número é par ou ímpar
def parouimpar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# b) Função que determina se um número é positivo ou negativo
def positivo(num):
    if num >= 0:
        return True
    else:
        return False

# c) Função que determina se um número é primo
def primo(num):
    ciclo = num
    divisor = 0

    while ciclo > 0:
        if num % ciclo == 0:
            divisor += 1
        ciclo -= 1

    if divisor == 2:
        return True
    else:
        return False

# d) Função que determina se um número é perfeito
def perfeito(num):
    soma_divisores = 0
    i = 0

    while i > 0:
        if num % i == 0:
            soma_divisores += i
        i += 1
    if soma_divisores == num:
        return True
    else:
        return False

# e) Função que determina se um número é triangular
def triangular(num):
    soma = 0
    n = 1

    while soma < num:
        soma += n
        n += 1

        if soma == num:
            return True
        else:
            return False


def testar_tudo():
    num = int(input("Introduza um número: "))

    # Testar se o número é par
    if parouimpar(num):
        print("O número é par")
    else:
        print("O número é impar")

    # Testar se o número é positivo
    if positivo(num):
        print("O número é positivo")
    else:
        print("O número é negativo")

    # Testar se o número é primo
    if primo(num):
        print("O número é primo")
    else:
        print("O número não é primo")

    # Testar se o número é perfeito
    if perfeito(num):
        print("O número é perfeito")
    else:
        print("O número não é perfeito")

    # Testar se o número é triângular
    if triangular(num):
        print("O número é triângular")
    else:
        print("O número não é triângular")
