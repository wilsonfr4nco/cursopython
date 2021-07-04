"""
Agrupamento só funciona se os itens estiverem incialmente ordenados.
"""

from itertools import groupby

alunos = [
    {'nome': 'Wilson', 'nota': 'A'},
    {'nome': 'Camila', 'nota': 'B'},
    {'nome': 'Ringo', 'nota': 'D'},
    {'nome': 'Jimmi', 'nota': 'D'},
    {'nome': 'Esher', 'nota': 'C'},
    {'nome': 'Kafka', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Clara', 'nota': 'A'},
    {'nome': 'Silvia', 'nota': 'B'},
    {'nome': 'Fabiano', 'nota': 'B'},
]
ordena = lambda item: item['nota']
print(ordena)
# Ordenando itens
alunos.sort(key=ordena)
print(alunos)
alunos_agrupados = groupby(alunos, ordena)
print(alunos_agrupados)
# no for abaixo vemos como foram agrupados os itens
# print('*** exibindo como foi feito o agrupamento dos itens da lista!')
# for agrupado in alunos_agrupados:
#     print(agrupado)

# print()
# print('Continuando o assunto...')
#
# for agrupamento, valores_agrupados in alunos_agrupados:
#     print(f'agrupamento: {agrupamento}')
#     for aluno in valores_agrupados:
#         print(aluno)
#     print()


# Sem tee (com list)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')


'''

 # Com tee
 for agrupamento, valores_agrupados in alunos_agrupados:
   v1, v2 = tee(valores_agrupados)
 
   print(f'Agrupamento: {agrupamento}')
 
   for aluno in v1:
     print(f'\t{aluno}')
 
   quantidade = len(list(v2))
   print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
'''
