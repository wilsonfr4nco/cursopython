"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str divide transformando em lista
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / para objetos iteráveis
"""
string = 'O Brasil é o o o o país do progresso, o Brasil é bom'
lista = string.split(' ') # removeu os espaços e fez uma lista com as palavras em os espaços
lista2 = string.split(',')
print(lista)
print(lista2)

palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A plavra que apareceu mais vezes é {palavra} ({contagem}x)')