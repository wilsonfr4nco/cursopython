"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
maior que 6 escreva "seu nome é muito grande".
"""

nome1 = input('Digite seu primeiro nome: ')
letras = len(nome1)

if letras <= 4:
    print('Seu nome é curto.')
elif 5 <= letras <= 6:
    print('Seu nome é de tamanho normal.')
else:
    print('Seu nome é muito grande.')
