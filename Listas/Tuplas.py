"A diferença da lista é que a tupla é imutável, ou seja, não pode ser alterada após sua criação."

tuplaLetras = ("A", "B", "C", "D", "E", "F")
print(tuplaLetras)

print(type(tuplaLetras))
print(len(tuplaLetras))  # Tamanho da tupla
print(tuplaLetras[0])  # Acessando o primeiro elemento
print(tuplaLetras[-1])  # Acessando o último elemento

print("\n")

NovaTupla = ("G", "H", "I")
print(NovaTupla)
print(type(NovaTupla))

tuplaLetras += NovaTupla  # Concatenando tuplas
print(tuplaLetras)

print("\n")

TuplaNumeros = (1, 2, 3, 4, 5)
print(TuplaNumeros)
ListaNumeros = list(TuplaNumeros)  # Convertendo tupla para lista
print(ListaNumeros)
ListaNumeros.remove(3)  # Removendo elemento da lista
TuplaNumeros = tuple(ListaNumeros)  # Convertendo lista de volta para tupla
print(TuplaNumeros)