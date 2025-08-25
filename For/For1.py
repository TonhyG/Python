ListaLetras = ['a', 'b', 'c', 'd']

#For = Para / loop exemplo
for letra in ListaLetras:
    print("A letra é:", letra)

print("\n\n")

for posicaoLetra, letra in enumerate(ListaLetras):
    print("A letra na posição", posicaoLetra, "é:", letra)

print("\n\n")

for i in "Python":
    print("A letra é:", i)

print("\n\n")

cor = "Azul", "Verde", "Amarelo"

for i in cor:
    if i == "Amarelo":
        print("A cor é:", i)
        break
