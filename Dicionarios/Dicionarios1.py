dicionario = {
    "Anthony": 19,
    "Bruna": 20,
    "Carlos": 21
}

print(dicionario)
print(len(dicionario)) # 3
print(type(dicionario)) # <class 'dict'>

print("\n")

dicionario2 = dicionario.copy() # Copia o dicionario
print(dicionario2)

dicionario3 = dict(dicionario) # Outra forma de copiar o dicionario
print(dicionario3)

print("\n")

pessoas = {
    "Ana": 21,
    "Bruno": 22,
    "Carlos": 23,
    "Bruno": 33
}

print(pessoas) # {'Ana': 21, 'Bruno': 33, 'Carlos': 23} - Chaves duplicadas são sobrescritas

dados = pessoas["Bruno"] # Acessa o valor pela chave
print(dados) # 33
dados2 = pessoas.get("Ana") # Outra forma de acessar o valor pela chave
print(dados2) # 21

nomes = pessoas.keys() # Retorna todas as chaves
print(nomes) # dict_keys(['Ana', 'Bruno', 'Carlos'])

idades = pessoas.values() # Retorna todos os valores
print(idades) # dict_values([21, 33, 23])

print("\n")

alimentos = {
    "arroz": 5.99,
    "feijao": 7.99,
    "macarrao": 4.99
}
print(alimentos)

#alterar o preço do arroz
alimentos["arroz"] = 6.99
print(alimentos)

#alterar o preço do feijão
alimentos.update({"feijao": 8.99})
print(alimentos)