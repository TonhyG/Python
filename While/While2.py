linha = 0

while linha < 5:
    coluna = 0
    while coluna < 5:
        print("Linha", linha, "Coluna", coluna)
        coluna += 1
    print()  # Pula para a próxima linha após completar as colunas
    linha += 1

print("\n")

inicio = 1
fim = int(input("Digite o número final: "))

while inicio <= fim:
    print(inicio)
    inicio += 1

print("\n\n")

numeoro = 1
numeroPar = int(input("Digite um número maior que 1: "))
while numeoro <= numeroPar:
    if numeoro % 2 == 0:
        print(numeoro)
    numeoro += 1