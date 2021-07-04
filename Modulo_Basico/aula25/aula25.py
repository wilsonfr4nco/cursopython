"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str divide transformando em lista
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / para objetos iteráveis
"""
string = 'O Brasil é o país do progresso, o Brasil é bom'
lista = string.split(' ') # removeu os espaços e fez uma lista com as palavras em os espaços
lista2 = string.split(',')
print(lista)
print(lista2)
print()
string = "tudo o que for dito dito dito e falado falado"
lista = string.split(sep=" ", maxsplit=4) #outra forma de usar o split

for valor in lista:
    print(f'A palavra {valor} apareceu {lista.count(valor)}x na frase')
for valor in lista2:
    print(f'A palavra {valor} apareceu {lista2.count(valor)}x na frase')