"""
While em python

Utilizado para realizar ações equanto uma condição for verdadeira.
O comando "continue" faz ignorar os próximos comandos abaixo dele
O comando "break" finaliza o loop
"""
x = 0

while x <= 9:
    if x == 3:
        x = x + 1
        continue
    elif x == 7:
        break

    print(x)
    x = x + 1
print('Acabou!')

