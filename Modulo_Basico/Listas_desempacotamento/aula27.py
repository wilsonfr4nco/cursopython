"""
Desempacotamento de listas em Python
"""

lista = ['ringo', 'escher', 'jimmi']

n1, n2, n3 = lista

print(n2)
print()

lista2 = ['ringo', 'escher', 'jimmi', 1, 2, 3, 4, 5, 6, 7]
n1, n2, *outralista = lista2
print(outralista) # primeira variável é n1, segunda variável é n2
# *outralista é uma segunda lista criada com os valores restantes

n1, n2, *outralista, ultimodalista = lista2


print(outralista) # mostra a lista menos os dois primeiros itens e o último
*outralista, n1,n2,n3 = lista2
print(outralista) # mostra a lista toda menos os 3 últimos valores

n1,n2,*_ = lista # ao utilizar " *_ " a variável funciona, mas é utilizada para
# indicar a outros desenvolvedores que você não vai utilizar este valor no seu código.