"""
Manipulando strings
* String indicies
* Fatiamento de strings {inicio:fim:passo}
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (tipos built-in)
"""

#       [012345678] positivo
texto = 'Python s2'
#      -[987654321] negativo
print(texto[2])
print(texto[-2])
print(texto[7])
nova_str = texto[2:7]
print(nova_str)
nova_str = texto[:6] # do inicio da string é só começar usando nada '0:6'
print(nova_str)
nova_str = texto[6:] # de um certo ponto até o final '6:final'
print(nova_str)
nova_str = texto[-1] # fintal da palavra
print(nova_str)