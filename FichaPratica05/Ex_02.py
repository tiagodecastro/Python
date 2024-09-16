def numeromaispequeno():
    num1 = int(input("Introduza um número: "))
    num2 = int(input("Introduza um número: "))
    num3 = int(input("Introduza um número: "))

    if num1 < num2 and num1 < num3:
        print(f"O número {num1} é o mais pequeno.")
    elif num2 < num1 and num2 < num3:
        print(f"O número {num2} é o mais pequeno.")
    elif num3 < num1 and num3 < num2:
        print(f"O número {num3} é o mais pequeno.")
    else:
        print("Há números iguais.")

numeromaispequeno()