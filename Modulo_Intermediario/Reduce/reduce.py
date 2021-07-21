"""
Função REDUCE, utilizada para acumular itens.

"""

from listas import produtos, pessoas, lista
# Essa função não vem por padrão, ou seja não é builtin, por isso precisamos importar ela
from functools import reduce

# exemplo de acumulação de itens

acumula = 0
for item in lista:
    acumula += item

print(acumula)

# agora utilizando a função reduce

# o "item" será a variável da interação.
# a lista será iterada e o valor "0" é o valor inicial da variável acumula
soma_lista = reduce(lambda acumula, item: item + acumula, lista, 0 )
print(soma_lista)
# mais um exemplo
soma_precos = reduce (lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)
#Abaixo dividimos os preço pela quantidade de produtos
print(soma_precos / len(produtos))


soma_idades = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idades)
print(f'{soma_idades / len(pessoas):.2f}')

