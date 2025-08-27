ListaNome = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
print(ListaNome)

print("\n\n")

Lista1 = ["a", "maça", "macaco", "jacu"]
Lista2 = [1, 2, 3, 4, 5]
Lista3 = ["fogo", "agua", "terra", "ar"]

print(Lista1)
print(Lista2)
print(Lista3)

print("\n\n")

print(Lista1[1])  # Acessa o segundo elemento da lista (índice 1)
print(Lista1[1:3])  # Acessa do segundo ao terceiro elemento (índices 1 a 2)
print(Lista1[:3])  # Acessa do início até o terceiro elemento (índices 0 a 2)
print(Lista1[2:])  # Acessa do terceiro elemento até o final (índice 2 em diante)
print(Lista1[-1])  # Acessa o último elemento da lista
print(Lista1[-3:])  # Acessa os três últimos elementos da lista
print(Lista1[:-2])  # Acessa todos os elementos, exceto os dois últimos
print(Lista1[::2])  # Acessa todos os elementos, pulando de 2 em 2
print(Lista1[::-1])  # Acessa todos os elementos em ordem reversa