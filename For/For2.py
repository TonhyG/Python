nomes = "Ana", "Carlos", "Maria", "João"

for nome in nomes:
    if nome == "Maria":
        continue  # pula o nome "Maria" e continua o loop
    print("O nome é:", nome)

print("\n\n")

for i in range(11):  # range(11) gera números de 0 a 10
    print("O número é:", i)

print("\n\n")

for i in range(1, 11, 1):  # range(início, fim, passo)
    print("O número é:", i)

print("\n\n")

for i in range(20, 9, -1):  # Contagem regressiva de 20 a 10
    print("O número é:", i)