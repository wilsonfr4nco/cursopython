"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
escrito, exiba a saudação apropriada
ex. Bom dia 0-11, boa tarde 12-17, boa noite 18-23
"""

hora = input("Digite a hora atual sem os minutos: ")

if not hora.isnumeric():
    print('Caractere inválido, digite a hora atual apenas!')
elif hora.isnumeric():
    hora2 = int(hora)
    if 0 <= hora2 <= 11:
        print('Bom dia!')
    elif 12 <= hora2 <= 17:
        print('Boa tarde!')
    elif 18 <= hora2 <= 23:
        print('Boa noite!')
    else:
        print('Digite uma hora entre 0 e 23!!')
