"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(
    indice,
    estados,
    cidades
)

print(cidades_estados) # mostra apenas o espaço da memória e não os valores

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)


#################################### zip longest ###############################################


indice2 = count() # <- se utilizar o count sem parâmetro teremos um loop infinito no zip longest
cidades2 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados2 = ['SP', 'MG', 'BA']

cidades_estados2 = zip_longest(
    indice2,
    estados2,
    cidades2,
    fillvalue='Estado' # caso não use esse item o valor será none.
)

for valor in cidades_estados2:
    print(valor)