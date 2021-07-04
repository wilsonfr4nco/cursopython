"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um
número inteiro, informe que não é um número inteiro
"""
num1 = input('Ditite um número inteiro: ')

if not num1.isnumeric():
    print('Caractere inválido, digite um número inteiro!')
elif num1.isnumeric():
     num2 = int(num1)
     parouimpar = (num2 % 2)

     if parouimpar == 0:
         print('O número digitado é par.')
     else:
         print('O número digitado é ímpar.')
