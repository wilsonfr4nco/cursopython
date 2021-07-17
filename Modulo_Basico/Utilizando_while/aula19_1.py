"""
While em python

Utilizado para realizar ações equanto uma condição for verdadeira.
O comando "continue" faz ignorar os próximos comandos abaixo dele
O comando "break" finaliza o loop
"""
x = 0 # coluna
y = 0 # linha

while x <= 10:
    y = 0

    while y <= 5:
        print(f'{x}, {y}')
        y += 1
    x += 1    # x = x + 1

print('Acabou!')
