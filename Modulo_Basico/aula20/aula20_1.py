"""

while / else
Contadores
Acumuladores
Se utilizar "break" os comandos que estão abaixo do "else" não serão executados.
"""
contador = 1
acumulador = 1
while contador < 10:
    print(contador, acumulador)

    if contador > 5:
        break
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')
print('Isso será executado.')