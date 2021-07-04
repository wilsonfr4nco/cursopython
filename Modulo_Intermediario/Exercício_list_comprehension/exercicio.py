"""
Exercício
Dada a string:
string = '0123456789012345678901234567890123456789012345678901234567890123456789'

Utilizando list comprehension transformar a string acima em:

lista = ['0123456789','0123456789','0123456789','0123456789','0123456789']

E depois transormar a lista acima em uma string conforme exemplo abaixo:

retorno = '0123456789.0123456789.0123456789.0123456789.0123456789.0123456789'
"""
string = '0123456789012345678901234567890123456789012345678901234567890123456789'

lista = [v.replace('9', '9i') for v in string]
lista = "".join(lista)
lista = lista.split('i')
*outralista, n1 = lista
print(outralista) # primeira resposta

lista2 = '.'.join(outralista)
print(lista2)

####################################################################################
# resposta do professor

string = '0123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
lista = [string[i:i + n] for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)

