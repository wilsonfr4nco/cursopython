"""
Operador ternário em Python
"""

logged_user = False

if logged_user:
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar.'
print(msg)

# simplificando o exemplo acima

logged_newuser = True
msg = 'Usuário logado.' if logged_newuser else 'Usuário precisa logar.'
print(msg)