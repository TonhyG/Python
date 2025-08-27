lista = ["A", "B", "C", "D", "E"]
lista2 = [1, 2, 3, 4, 5]

lista.extend(lista2)  # Adiciona os elementos de lista2 ao final de lista
print("Lista após extend:", lista)

lista.remove("C")  # Remove o elemento "C" da lista
print("Lista após remove 'C':", lista)

lista.pop(2)  # Remove o elemento no índice 2 (terceiro elemento)
print("Lista após pop índice 2:", lista)

lista.pop()  # Remove o último elemento da lista
print("Lista após pop último elemento:", lista)

del lista[0]  # Remove o elemento no índice 0 (primeiro elemento)
print("Lista após del índice 0:", lista)

lista.clear()  # Remove todos os elementos da lista
print("Lista após clear:", lista)

lista.append("F")  # Adiciona o elemento "F" ao final da lista
print("Lista após append 'F':", lista)

lista.insert(1, "Goiaba") # Adiciona "Goiaba" na posição de índice 1
print("Lista após insert 'Goiaba' no índice 1:", lista)

lista.insert(1, "Araçoiaba") # Adiciona "Goiaba" na posição de índice 1
print("Lista após insert 'Araçoiaba' no índice 1:", lista)

if "Goiaba" in lista:
    print("Goiaba está na lista.")
else:
    print("Goiaba não está na lista.")

lista[2] = "Melancia"  # Altera o elemento no índice 2 para "Melancia"
print("Lista após alterar índice 2 para 'Melancia':", lista)

lista[1:3] = ["Laranja", "Uva"]  # Altera os elementos nos índices 1 e 2
print("Lista após alterar índices 1 e 2 para 'Laranja' e 'Uva':", lista)