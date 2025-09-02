"""
add() - Adiciona um elemento ao conjunto.
union() - Retorna a união de dois conjuntos.
intersection() - Retorna a interseção de dois conjuntos.
difference() - Retorna a diferença entre dois conjuntos.
discard() - Remove um elemento do conjunto, se existir.
clear() - Remove todos os elementos do conjunto.
summetric_difference_update() - Atualiza o conjunto com a diferença simétrica entre ele e outro conjunto.
summetric_difference() - Retorna a diferença simétrica entre dois conjuntos.
"""

#Add = Adiciona um elemento ao conjunto
setExemplo1 = set()
setExemplo1.add(1)
setExemplo1.add(2)
setExemplo1.add(3)
setExemplo1.add("aaaaa")
print(setExemplo1) # {1, 2, 3, 'aaaaa'}

print("\n")

setExemplo2 = {"a", "b", "c"}
print(setExemplo2)

print("\n")

#union = Retorna a união de dois conjuntos
setA = {1, 2, 3}
setB = {"Otavio", "Ana", "Maria"}
setC = setA.union(setB)
print(setC) # {1, 2, 3, 'Otavio', 'Ana', 'Maria'}

print("\n")

#intersection = Retorna a interseção de dois conjuntos
ListaSets1 = {"Python", "Java", "C#", "JavaScript"}
ListaSets2 = {"VisualG", "Lógica", "Python"}

ImprimirOsDois = ListaSets1.union(ListaSets2)
print(ImprimirOsDois) # {'Python'}

ValorEmAmbos = ListaSets1.intersection(ListaSets2)
print(ValorEmAmbos) # {'Python'} retorna apenas o que tem em ambos

print("\n")

#summetric_difference_update = Atualiza o conjunto com a diferença simétrica entre ele e outro conjunto
ListaSets1.symmetric_difference_update(ListaSets2)
print(ListaSets1) # {'Java', 'C#', 'JavaScript', 'VisualG', 'Lógica'}

print("\n")

#summetric_difference = Retorna a diferença simétrica entre dois conjuntos
ListaSets3 = {"Python", "Java", "C#", "JavaScript"}
ListaSets4 = {"VisualG", "Lógica", "Python"}
ValorEmAmbos2 = ListaSets3.symmetric_difference(ListaSets4)
print(ValorEmAmbos2) # {'Java', 'C#', 'JavaScript', 'VisualG', 'Lógica'}

print("\n")

setNumeros = {1, 2, 3, 3, 4, 5}
print(setNumeros) # {1, 2, 3, 4, 5} repetições são ignoradas
