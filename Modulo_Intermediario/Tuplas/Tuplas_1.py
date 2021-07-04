"""
Tuplas
"""

t1 = (1,2,3, 'a', 'Wilson') * 10  # repetindo a sequência 10 vezes
# t1[1] = 3 <- essa linha se colocada dará erro pois o valor da tupla não pode ser alterado
print(t1)
t1= list(t1) # transformei a tupla em lista
print(t1)
ti = tuple(t1) # voltou a ser tupla


