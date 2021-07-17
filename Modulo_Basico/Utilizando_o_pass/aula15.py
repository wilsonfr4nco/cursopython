"""
Quando se quer deixar parte do código para escrever depois e não dar erro
"""
# O código abaixo dará erro por conta do comentário após o if
# valor = True

# if valor:
    # escrever depois
# else:
#    print('bye')

# para contornar o erro acima basta usar o comando "pass" pode ser usado também "..."
valor = True

if valor:
    pass
else:
    print('bye')
