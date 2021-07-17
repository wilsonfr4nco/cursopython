"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str divide transformando em lista
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / para objetos iteráveis
"""
string = 'O Brasil é progresso.'
lista = string.split(' ')
string2 = ','.join(lista) # une os itens da lista com o caractere entre aspas

print(string)
print()
print(lista)
print()
print(string2)
