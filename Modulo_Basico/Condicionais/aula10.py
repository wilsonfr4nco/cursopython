"""
Condicionais IF, ELIF e ELSE
"""

idade = (int(input("digite sua idade: ")))
acesso = idade >= 18
adole = 18 > idade > 12

if acesso:
    print('Você é maior de 18 anos, pode entrar na sala dos adultos')
elif adole:
    print('você pode entrar na sala de jovens')
    nome = input('Digite seu nome: ')

    print(f'Seu nome é {nome}')
else:
    print('vá procurar papai e mamãe.')
