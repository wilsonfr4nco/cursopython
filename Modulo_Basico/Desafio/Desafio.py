#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
"""
CPF = 168.995.350-09
---------------------------------------------------------------

1 * 10 = 10          #    1 * 11 = 11 <-
6 * 9  = 54          #    6 * 10 = 60
8 * 8  = 64          #    8 * 9  = 72
9 * 7  = 63          #    9 * 8  = 72
9 * 6  = 54          #    9 * 7  = 63
5 * 5  = 25          #    5 * 6  = 30
3 * 4  = 12          #    3 * 5  = 15
5 * 3  = 15          #    5 * 4  = 20
0 * 2  = 0           #    0 * 3  = 0
                     # -> 0 * 2  = 0
         297         #             343
11 - (297 % 11) = 11 #      11 - (343 % 11) = 9
11 > 9 = 0           #
Digito 1 = 0         #    Digito 2 = 9
"""

cpf = input('Digite o CPF apenas com números: ')

# Primeira conta ======================================================
contar = 0
multiplic = 11
soma = 0

for numero in cpf:
    cpf[contar]
    contar += 1
    multiplic -= 1
    soma = soma + (int(numero) * multiplic)
    if contar == 9:
        break

# Primeiro dígito =====================================================
digito1 = 11 - (soma % 11)

if digito1 > 9:
    digito1 = 0

# Segunda soma ========================================================
multiplic = 12
soma = 0
contar = 0

for numero in cpf:
    cpf[contar]
    contar += 1
    multiplic -= 1
    soma = soma + (int(numero) * multiplic)
    if contar == 9:
        soma = soma + (digito1 * 2)
        break

# Segundo dígito ======================================================
digito2 = 11 - (soma % 11)

if digito2 > 9:
    digito2 = 0

# Validação do CPF ====================================================
cpf_valido = cpf[:9] + str(digito1) + str(digito2)

if cpf_valido == cpf:
    print('O CPF digitado é válido!')
else:
    print('O CPF digitado é inválido!!!!')
