"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

Resposta:
Wilson tem x anos, x de altura e pesa xKg.
O IMC de Wilson é x.
Wilson nasceu em x.
"""
nome = 'Wilson'
idade = 43
altura = 1.78
peso = 83.0
ano = 2021
nasc = ano - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} altura e pesa {peso}Kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nasc}.')
