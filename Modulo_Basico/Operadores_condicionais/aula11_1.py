"""
operadores relacionais + IF, ELIF e ELSE
== igual
> maior
>= maior ou igual
< menor
<= menor ou igual
!= diferente
"""
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar empréstimo.')
else:
    print(f'{nome} você não pode pegar empréstimo')