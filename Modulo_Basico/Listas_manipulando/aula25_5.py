"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str divide transformando em lista
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / para objetos iteráveis
"""
lista = [
    [1,2],
    [3,4],
    [5,6],
]
l1, l2, l3 = lista

print(l1)
for v in lista:
    print(v)
    print(v[0], v[1]) # acessar o índice  apenas

lista2 = ['wilson', 'camila', 'casa']
n1, n2, n3 = lista2

print()
print(n2)