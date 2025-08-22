"""
While  = Enquanto / loop exemplo
"""

numero = 1

while numero <= 10:
    print("O número é:", numero)
    numero += 1  # mesma coisa que numero = numero + 1

print("\n\n")

contador = 1

while contador <= 5:
    print("Contador é:", contador)
    if contador == 3:
        print("Contador é igual a 3, saindo do loop.")
        break # sai do loop quando contador é 3
    contador += 1

print("\n\n")

numero2 = 3

while numero2 <= 30:
    print("Número2 é:", numero2)
    if numero2 == 15:
        print("Número2 é igual a 15, pulando para o próximo número.")
        numero2 += 1
        continue # pula o resto do código e volta para o início do loop
    numero2 += 3