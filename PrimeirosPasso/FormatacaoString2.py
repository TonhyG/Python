palavraComEspaço = "                Aprendedendo Python           "  # Declaração de variável com espaços em branco
print(palavraComEspaço)

print(palavraComEspaço.strip())  # Remove espaços em branco no início e no final da string

print("\n\n")  # Pula duas linhas para melhor visualização

gostoPorFrutas = "Eu gosto de maçã, banana, laranja e abacaxi."  # Declaração de variável com frase
print(gostoPorFrutas)
print("jabuticaba" in gostoPorFrutas)  # Verifica se "jabuticaba" está presente na string (retorna False)
print("banana" in gostoPorFrutas)  # Verifica se "banana" está presente na string (retorna True)
print("banana" not in gostoPorFrutas)  # Verifica se "banana" não está presente na string (retorna False)
print("jabuticaba" not in gostoPorFrutas)  # Verifica se "jabuticaba" não está presente na string (retorna True)

procuraLetra = gostoPorFrutas.find("o")  # Encontra a posição da primeira ocorrência de "o" na string
print(procuraLetra)

print("\n\n")

aluno = "Anthony Guilherme"  # Declaração de variável com nome do aluno
Nota1 = 8.5  # Declaração de variável com nota 1
Nota2 = 9.0  # Declaração de variável com nota 2
media = (Nota1 + Nota2) / 2  # Cálculo da média das notas
print("O aluno " + aluno + " obteve a média de " + str(media) + " nas notas " + str(Nota1) + " e " + str(Nota2) + ".")  # Exibe a mensagem formatada com o nome do aluno e as notas
print(f"O aluno {aluno} obteve a média de {media} nas notas {Nota1} e {Nota2}.")  # Exibe a mensagem formatada usando f-strings
print("O aluno {} obteve a média de {} nas notas {} e {}.".format(aluno, media, Nota1, Nota2))  # Exibe a mensagem formatada usando o método format