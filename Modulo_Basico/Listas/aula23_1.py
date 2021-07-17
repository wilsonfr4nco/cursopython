"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""


l1 = [1,2,3]
l2 = [4,5,6]
l4 = [7,8,9]
l5 = [9,10,11]
l3 = l1 + l2 # concatenar listas
l3.clear() # limpar todos os valores da lista l3
l1.extend(l2) # expandir a lista l1 com a l2
l1.extend('a') # pode adicionar vários valores
l2.append('b') # adiciona apenas um valor
l1.extend(l2)
l4.insert(0, 'inserir')


print(l1)
print(l2)
print(l3)
print(l4)