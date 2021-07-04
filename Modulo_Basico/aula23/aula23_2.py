"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""


l1 = [1,2,3,4,5,6,7,8,9]
print(l1)
l1.insert(0, 'banana')
print(l1)
l1.pop() # se não definir o indice o valor deletado é o do último índice
print(l1)
del(l1[3:5]) # será apagado os valores do índice 4 e 5
print(l1)