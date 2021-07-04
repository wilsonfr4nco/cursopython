"""
Operador ternário em Python
"""
idade = 18

if idade >= 18:
    print('Pode acessar.')
else:
    print('Não pode acessar.')

# simplificando abaixo usando operador ternário

idade = 17
maior = (idade >= 18)
msg = 'Pode acessar' if maior else 'Não pode acessar.'

print(msg)