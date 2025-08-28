ListaNome = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']

for i in ListaNome:
    print(i)

print("\n")

[print(i) for i in ListaNome]

print("\n")

ListaNomeU = []
for i in ListaNome:
    if "u" in i:
        ListaNomeU.append(i)
print(ListaNomeU)