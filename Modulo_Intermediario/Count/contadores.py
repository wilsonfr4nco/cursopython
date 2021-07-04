"""
count - Itertools
O count sem valor definido permanece contando infinitamente.

"""
from itertools import count

contador = count(start=5, step=0.1) # pode ser também count(5, 0.1)

for valor in contador:
    print(round(valor, 2)) # round faz o arredondamento de casas decimais que está especificada no número 2

    if valor >= 10: # utilizado para interromper o count
        break

#################  contagem decrescente ####################

contador2 = count(start=10, step=-1)

for valor in contador2:
    print(valor)

    if valor <= -10:
        break



