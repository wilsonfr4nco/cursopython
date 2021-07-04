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

idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar empréstimo.')
else:
    print(f'{nome} você não pode pegar empréstimo')