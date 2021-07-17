"""
Formatando valores com modificadores - Aula5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO):f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}' .format(divisao)) # Representar o número com duas casas decimais
print(f'{divisao:.2f}') # Representar o número com duas casas decimais
print()
num_1 = 10
num_2 = 3
num_3 = 1
divisao = num_1 / num_2
print(f'{num_1:0<10}') # Número representando com 10 caractares que são a soma do númeor da variável mais os zeros indicados na função. (os número adicionados ficam à direita)
print(f'{num_3:0^9}') # Número representando com 9 caractares que são a soma do númeor da variável mais os zeros indicados na função. (os zeros centralizam o número da variável)
print(f'{num_3:.2f}')
print(f'{num_3:0>10.2f}')
print('{:.2f}' .format(divisao))
print(f'{divisao:.2f}')
nome = 'Wilson Franco'
print(f'{nome:#^50}') # Printa o nome no centro e os # à direita e esquerda.
nome_form = '{:@>50}'.format(nome)
print(nome_form)
nome_form = '{n}{n}{n}'.format(n=nome)
print(nome_form)
nome_form = '{n:0<20}'.format(n=nome)
print(nome_form)
# índice
nome = 'Wilson'
sobrenome = 'FrANco'
nome_form = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
print(nome_form)
print(nome_form.lower())
print(nome_form.upper())
print(nome_form.title())
print(nome_form.ljust(20, "#"))
