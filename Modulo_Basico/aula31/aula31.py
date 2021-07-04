"""
Criar uma estrutura de repetição utilizando os dois contadores.
A cada volta do laço um contador de maneira progressiva e o outro de maneira regressiva.
usar FOR / WHILE

0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
string = '10 9 8 7 6 5 4 3 2'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(f'{indice} {valor}')
