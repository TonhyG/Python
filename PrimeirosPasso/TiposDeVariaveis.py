"""
str = String / textos
int = Inteiros / números inteiros
float = Números decimais
bool = Booleano / Verdadeiro ou Falso
list = Lista / Coleção de valores
"""

nome = type("Anthony")  # Tipo da variável nome
print(nome)  # Exibe o tipo da variável nome

idade = type(20)  # Tipo da variável idade
print(idade)  # Exibe o tipo da variável idade

altura = type(1.75)  # Tipo da variável altura
print(altura)  # Exibe o tipo da variável altura

namorado = type(True)  # Tipo da variável namorado
print(namorado)  # Exibe o tipo da variável namorado

testelista = [1, 2, 3,]
lista = type(testelista)  # Tipo da variável lista
print(lista)  # Exibe o tipo da variável lista

print("\n\n")

print("Anthony", type("Anthony"))  # Exibe o valor e o tipo da variável nome
print(20, type(20))  # Exibe o valor e o tipo da variável idade
print(1.75, type(1.75))
print(True, type(True))  # Exibe o valor e o tipo da variável namorado
print([1, 2, 3], type([1, 2, 3]))  # Exibe o valor e o tipo da variável lista
