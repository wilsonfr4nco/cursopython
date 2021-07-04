"""
Entrada de dados (input)
"""

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
nasc = 2021-int(idade)  # mudei a variável para inteiro, pois input é só para string

print()
print(f'Seu nome é: {nome}')
print(f'Sua idade é: {idade}')
print()
print(f'O usuário digitou {nome} e o tipo da variável é '
      f'{type(nome)}')
print()
print(f'{nome} tem {idade} anos. \n'
      f'{nome} nasceu em {nasc}.')
