"""
Utiliza-se while quando não se sabe quando vai terminar.
while / else

Contadores
Acumuladores
"""
contador = 1
acumulador = 1
while contador < 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
