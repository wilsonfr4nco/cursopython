"""
Enumerate - Enumerar elementos da lista # list
"""

lista = [
    ['edu', 'joao', 'luiz'],
    ['maria', 'aline', 'joana'],
    ['helena', 'ed', 'lu'],
]

print(lista[2]) # print lista indice 2
print(lista[1][2]) # print lista mãe indice 1, elemento da lista filha indice 2

enumerada = enumerate(lista)
print(enumerada) # aparece um objeto enumerate <enumerate object at 0x7f8570bd2280>
print()

print(list(enumerada))
enumerada = list(enumerate(lista))
# resultado do print:
# 0     1       <--- Índices
# [(0, ['edu', 'joao', 'luiz']), # 0
#         0        1          2
# (1, ['maria', 'aline', 'joana']), # 1
# (2, ['helena', 'ed', 'lu'])] # 2

print(enumerada[1][0]) # resultado é 1, primeiro é o índice da lista mãe e depois da filha
print(enumerada[1][1][2]) # lista dentro de lista, do índice mais amplo até o mais restrito



