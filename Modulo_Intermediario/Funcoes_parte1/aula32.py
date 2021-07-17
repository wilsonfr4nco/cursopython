"""
Funções - def em Python (parte 1)
"""

def funcao(msg, nome):
    nome = nome.replace('e', '3') # quando encontrar letra 'e' será substituido por '3'
    print(msg, nome)

funcao('ola', 'wilson')


def saudacao(msg='ola', nome='wilson'): # valor padrão "ola" e "wilson", caso não sejam estabelecidos valores.
    nome = nome.replace('e', '3')
    print(msg, nome)

saudacao(nome='Camila', msg='oi donguinha') # A mensagem vai aparecer na ordem que foram criadas na funcao
saudacao('Olá', 'Tico')
saudacao('Escola', 'Tem coisa boa')
