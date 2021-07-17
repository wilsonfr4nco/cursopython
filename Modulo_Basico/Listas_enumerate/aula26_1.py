"""
Enumerate - Enumerar elementos da lista # list

DESEMPACOTAMENTO
"""

lista = [
    ['edu', 'joao', 'luiz'],
    ['maria', 'aline', 'joana'],
    ['helena', 'ed', 'lu'],
]

for v1, v2 in enumerate(lista, 53): # enumerate iniciando de 53
    print(v1, v2)
# Resultado:
# 53 ['edu', 'joao', 'luiz']
# 54 ['maria', 'aline', 'joana']
# 55 ['helena', 'ed', 'lu']

print()

for v1 in enumerate(lista, 53):
    print(v1)

# Resultado:
# (53, ['edu', 'joao', 'luiz'])
# (54, ['maria', 'aline', 'joana'])
# (55, ['helena', 'ed', 'lu'])

print()

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    # print(valor_enumerado, minha_lista)
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3)