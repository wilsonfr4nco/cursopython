"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str divide transformando em lista
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / para objetos iteráveis
"""
string = 'O Brasil é progresso.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(f'{indice} é {valor} {lista[indice]}')


