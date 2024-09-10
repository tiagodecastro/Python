# Ler nota1
print("Introduza a primeira nota: ")
nota1 = float(input())
nota1 = nota1 * 0.25

# Ler nota2
print("Introduza a seguunda nota: ")
nota2 = float(input())
nota2 = nota2 * 0.35

# Ler nota3
print("Introduza a terceira nota: ")
nota3 = float(input())
nota3 = nota3 * 0.4

# Calcular Nota Final
notafinal = nota1 + nota2 + nota3

# Verificar se Aluno está Aprovado ou Reprovado
if notafinal >= 9.5:
    print(f"Aluno passou: {notafinal}")
elif notafinal < 9.5:
    print(f"Aluno reprovou: {notafinal}")