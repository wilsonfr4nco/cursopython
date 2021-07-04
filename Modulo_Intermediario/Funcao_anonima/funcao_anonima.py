"""
Função anônima
"""

def funcao(arg, arg2):
    return arg * arg2
var = funcao(10, 4)
print(var)


a = lambda x, y: x * y # Uma função anõnima igual a de cima só que é anônima pois não tem um nome
print(a(10,4))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]
def func(item):
    return item[1]

lista.sort(key=func) # o ordenamento acontece pois a função seleciona o índice 1 da lista acima.
print(lista)
lista.sort(key=func, reverse=True) # Com o reverse=True a lista aparece do maior para o menor
print(lista)


# Fazendo o exercicio acima utilizando função lambda.

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]


lista.sort(key=lambda item: item[1]) # o ordenamento acontece pois a função seleciona o índice 1 da lista acima.
print(lista)
lista.sort(key=lambda item: item[1], reverse=True) # Com o reverse=True a lista aparece do maior para o menor
print(lista)
print()
print()
print(sorted(lista, key=lambda i: i[1])) # Outra forma de utilizar o sorted
print(sorted(lista, key=lambda i: i[0], reverse=True)) # Ordenando pelo nome