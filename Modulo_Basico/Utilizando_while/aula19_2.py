"""
While em python

Utilizado para realizar ações equanto uma condição for verdadeira.
O comando "continue" faz ignorar os próximos comandos abaixo dele
O comando "break" finaliza o loop
"""

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not  num_1.isnumeric() or not num_2.isnumeric():
        print('Digite um número e não outro tipo de caractere!')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)


    # + - / *
    if operador == '+':
        print(f'O resultado da soma é {num_1 + num_2}')
    elif operador == '-':
        print(f'O resultado da soma é {num_1 - num_2}')
    elif operador == '*':
        resultado = num_1 * num_2
        print(f'O resultado da soma é {num_1 * num_2}')
    elif operador == '/':
        resultado = num_1 / num_2
        print(f'O resultado da soma é {num_1 / num_2}')
    else:
        print('Operador inválido!')
    print()
    sair = input('Deseja sair? Digite [s] para sim e [n]')

    if sair == 's':
        break

print('Acabou!')
