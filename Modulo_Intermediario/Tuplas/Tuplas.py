"""
Tuplas
"""

t1 = (1,2,3, 'a', 'Wilson') # tupla
t2 = 1, 2, 'a', 'Camila' # tupla
t3 = 1, # tupla

t4 = t1 + t2 + t3 # concatenar tuplas

n1, n2, n3, *_ = t4 # desempacotar em variáveis as tublas o "*_" desempacota o resto da tupla
n1, n2, n3, *_, n10 = t4 # O n10 recebe o útimo valor da tupla
print(type(t1))
print(type(t2))
print(type(t3))
print()
print(t4)
print(*_)


