"""
For / Else em python
continue e break tem o mesmo efeito utilizando o for
"""
# a função .startswith() verifica se uma palavra string começa com uma letra específica.
# a função .lower() coloca todas as letras em minúsculo
# variavel = ['wilson', 'camila', '321']
# comeca_comW = False
#
# for valor in variavel:
#     if valor.lower().startswith('w'):
#         comeca_comW = True
#
# if comeca_comW:
#     print('Existe uma palavra que começa com w')
# else:
#     print('Não existe plavra que começa com w')
# código abaixo igual ao código acima
variavel = ['awilson', 'camila', '321']


for valor in variavel:
    if valor.lower().startswith('w'):
        break
else:
    print('Não existe plavra que começa com w')