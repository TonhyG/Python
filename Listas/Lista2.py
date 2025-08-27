ListaMinMax = [10, 20, 30, 40, 50]

print("Maior valor:", max(ListaMinMax))
print("Menor valor:", min(ListaMinMax))

print("\n")

ListaNumeros1ate10 = [i for i in range(100)]  # Lista de 0 a 99
print("Lista de 0 a 99:", ListaNumeros1ate10)

print("\n")

Lista2em2 = [i for i in list(range(0, 101, 2))]  # Lista de 0 a 100 de 2 em 2
print("Lista de 0 a 100 de 2 em 2:", Lista2em2)

print("\n")

ListaOriginal = ["Carros", "Aviões", "Navios", "Motos"]
ListaCopiada = ListaOriginal.copy()  # Cópia da lista original
print("Lista Copiada:", ListaCopiada) 

print("\n")

l1 = [1, 2, 3]
l2 = ["A", "B", "C"]

for item in l2:
    l1.append(item)  # Adiciona cada item de l2 ao final de l1
    print("Lista l1 após adicionar", item, ":", l1)