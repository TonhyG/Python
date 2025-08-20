nome = "Anthony Guilherme"  # Declaração de variável com nome completo

print(nome)  # Exibe o nome completo

print("Total de caracteres:", len(nome))  # Exibe o total de caracteres na string
print(nome[0])  # Exibe o primeiro caractere da string
print(nome[0:7])  # Exibe os caracteres do índice 0 ao 6 (7 não incluído)

print("\n\n")  # Pula duas linhas para melhor visualização

frase = "PYTHON é uma LINGUAGEM de programação INCRÍVEL!"  # Declaração de variável com frase
print(frase.lower())  # Converte toda a string para minúsculas
print(frase.upper())  # Converte toda a string para maiúsculas
print(frase.title())  # Converte a primeira letra de cada palavra para maiúscula
print(frase.capitalize())  # Converte a primeira letra da string para maiúscula
print(frase.strip())  # Remove espaços em branco no início e no final da string

print("\n\n")  # Pula duas linhas para melhor visualização

frase2 = "Preciso conseguir 100mil"
print(frase2.replace("100mil", "1.000.000"))  # Substitui "100mil" por "100.000" na string
print(frase2.replace("100mil", "muito dinheiro"))  # Substitui "100mil" por "muito dinheiro" na string

print("\n\n")  # Pula duas linhas para melhor visualização

cpf = "123.456.789-00"  # Declaração de variável com CPF
cpfPartes = cpf.split(".")  # Divide a string CPF em partes usando o ponto como delimitador
print(cpfPartes[0])  # Exibe a primeira parte do CPF
print(cpfPartes[1])
print(cpfPartes[2])  # Exibe a segunda parte do CPF

print(cpf.split("-")[1])  # Divide a string CPF usando o hífen como delimitador e exibe a segunda parte

print("\n\n")  # Pula duas linhas para melhor visualização

cpf = "123.456.789-00"  # Declaração de variável com CPF
cpfCorte = cpf.split(".")  # Divide a string CPF usando o hífen como delimitador
print("CPF: " + cpfCorte[0] + cpfCorte[1] + cpfCorte[2])

