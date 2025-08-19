nome = "Anthony"
print(nome)  # Função print exibe o valor na tela

AC1 = AC2 = AC3 = AF = 0

AC1 = input("Digite a nota da AC1: ")
print(AC1)  # Exibe o valor da variável AC1

AC2 = input("Digite a nota da AC2: ")
print(AC2)  # Exibe o valor da variável AC2

AC3 = input("Digite a nota da AC3: ")
print(AC3)  # Exibe o valor da variável AC3

AF = input("Digite a nota da AF: ")
print(AF)  # Exibe o valor da variável AF

media = (float(AC1) + float(AC2) + float(AC3) + float(AF)) / 4
print("A média é:", media)  # Exibe a média das notas