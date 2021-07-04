d1 = {1 : 'a', 2 : 'b', 3: 'c', 4: ['wilson', 'franco']}
v = d1 # normalmente o valor na variável cria um novo valor, mas em python não é assim
# quando se utiliza o sinal de '=' não está sendo criado um novo objeto
# mesmo lugar na memória

print(d1)
print(v)

print()
v[1] = 'wilson' # se colocar esse valor novo, o dicionario d1 é alterado também

print(d1)
print(v)

print()

v2 = v.copy() # cópia rasa, pois são apenas uma referência nesta variável
v2[1] = 'camila'

print(v)
print(v2)
print()

d2 = {1 : 'a', 2 : 'b', 3: 'c', 'd': ['wilson', 'franco']}
v = d2.copy()

print(v['d'][0])
v['d'][0] = 'tico' # prova da cópia rasa.

print(d2)
print(v)

# cópia real usando o módulo copy

import copy

d2 = {1 : 'a', 2 : 'b', 3: 'c', 'd': ['wilson', 'franco']}
v = copy.deepcopy(d2)

print(v['d'][0])
v['d'][0] = 'tico' # cópia real

print(d2)
print(v)

#################################################################

d2 = {1 : 'a', 2 : 'b', 3: 'c', 'd': ('wilson', 'franco')}
v = copy.deepcopy(d2)

print(v['d'][0])
v['d'] = ('franco', 'wilson') # a tupla não se altera, mas o item inteiro pode ser...
# ...trocado por outro item.

print(d2)
print(v)
