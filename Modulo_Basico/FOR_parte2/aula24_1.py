"""
For / Else em python
continue e break tem o mesmo efeito utilizando o for
"""
# a função .startswith() verifica se uma palavra string começa com uma letra específica.
variavel = ['wilson', 'camila', '321']

for valor in variavel:
    if valor.startswith('c'):
        print('Começa com c ', valor)
    else:
        print('Não começa com c', valor)