"""

dict comprehension, permite uma manipulação mais livre do selementos de um dicionário.
"""

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x: y for x, y in lista} # fazendo dict comprehension
d2 = {x: y*2 for x, y in lista} # manipulando
d3 = {x.upper(): y.upper() for x, y in lista} # manipulando
d4 = {x: y for x, y in enumerate(range(5))} # manipulando
d5 = {x for x in range(5)} # não é um dicionário e sim um set
d6 = {f'chave_{x}': x**2 for x in range(5)} # dicionário
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)