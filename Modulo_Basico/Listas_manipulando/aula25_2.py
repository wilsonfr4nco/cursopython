"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str divide transformando em lista
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / para objetos iteráveis
"""
string = 'O Brasil é o o o o país do progresso, o Brasil é bom'
lista = string.split(' ') # removeu os espaços e fez uma lista com as palavras em os espaços
lista2 = string.split(',')
print(string.strip('O B')) # pode tirar caracteres na ordem em que aparecem nas extremidades
for valor in lista2:
    print(valor.strip()) # função .strip() remove o espaço ou caracter no inicio e fim da string
    print(valor.strip().capitalize()) # deixar a primeira letra maiúscula
    print(valor.strip(' Brs'))

