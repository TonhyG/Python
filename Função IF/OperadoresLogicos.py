"""
Operadores relacionais em Python
and conjunção (e)
or disjunção (ou)
not negação (não)
"""

numero1 = 10
numero2 = 20
numero3 = 30
numero4 = 40

if numero1 < numero2 and numero3 < numero4:
    print("As duas condições são verdadeiras.")

if numero1 < numero2 or numero3 > numero4:
    print("Pelo menos uma das condições é verdadeira.")

if not numero1 > numero2:
    print("A condição é falsa, então a negação é verdadeira.")

print("\n\n")

nota = input("Digite a nota do aluno: ")

if float(nota) >= 7:
    print("Aprovado")
elif float(nota) >= 5:
    print("Recuperação")
else:
    print("Reprovado")