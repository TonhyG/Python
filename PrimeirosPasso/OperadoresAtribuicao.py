"""
= numero = 1 / atribui o valor 1 à variável numero
+= numero += 1 / adiciona 1 ao valor atual da variável numero
-= numero -= 1 / subtrai 1 do valor atual da variável numero
*= numero *= 2 / multiplica o valor atual da variável numero por 2
/= numero /= 2 / divide o valor atual da variável numero por 2
%= numero %= 3 / atribui o resto da divisão do valor atual da variável numero por 3
**= numero **= 2 / eleva o valor atual da variável numero ao quadrado
//= numero //= 2 / divide o valor atual da variável numero por 2 e descarta a parte decimal
"""

numero = 10
print(numero)  # Exibe o valor inicial da variável numero

numero += 1  # Adiciona 1 ao valor atual da variável numero
print(numero)  # Exibe o novo valor da variável numero

numero -= 1  # Subtrai 1 do valor atual da variável numero
print(numero)  # Exibe o novo valor da variável numero

numero = 10  # Reinicia o valor da variável numero para 10

numero *= 2  # Multiplica o valor atual da variável numero por 2
print(numero)  # Exibe o novo valor da variável numero

numero /= 2  # Divide o valor atual da variável numero por 2
print(numero)  # Exibe o novo valor da variável numero

numero %= 3  # Atribui o resto da divisão do valor atual da variável numero por 3
print(numero)  # Exibe o novo valor da variável numero

print("\n\n")  # Pula duas linhas para melhor visualização

numero = 10  # Reinicia o valor da variável numero para 10

numero **= 2  # Eleva o valor atual da variável numero ao quadrado
print(numero)  # Exibe o novo valor da variável numero

numero = 10  # Reinicia o valor da variável numero para 10

numero //= 2  # Divide o valor atual da variável numero por 2 e descarta a parte decimal
print(numero)  # Exibe o novo valor da variável numero

print("\n\n")  # Pula duas linhas para melhor visualização

numero = 10  # Reinicia o valor da variável numero para 10
numero *= 2  # Multiplica o valor atual da variável numero por 2, mas não altera o valor da variável
print(numero)  # Exibe o valor original da variável numero, que permanece inalterado
