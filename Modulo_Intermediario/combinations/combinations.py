"""
Combinations, permutations e product - Itertools
Combinação - Ordem dos itens não importa
Permutação - Ordem dos itens importa
Combinação e permutação não repetem valores únicos.
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product
############### Combinations

pessoas = ['Wilson', 'Camila', 'Kafka', 'Ringo', 'Esher', 'Jimmi']

for grupo in combinations(pessoas, 2): # irá realizar combinações de 2 em 2
    print(grupo)

############### Permutation

pessoas = ['Wilson', 'Camila', 'Kafka', 'Ringo', 'Esher', 'Jimmi']

for grupo in permutations(pessoas, 2): # irá realizar combinações de 2 em 2
    print(grupo)

############### Product

pessoas = ['Wilson', 'Camila', 'Kafka', 'Ringo', 'Esher', 'Jimmi']

for grupo in product(pessoas, repeat=2): # irá realizar combinações de 2 em 2
    print(grupo)