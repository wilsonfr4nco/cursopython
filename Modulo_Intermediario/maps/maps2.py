'''
Com listcomprehension raramente precisa-se utilizar função lambda
'''

from maps import produtos, pessoas, lista

# nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista] # mesmo exemplo de cima com listcomprehension
print(lista)
print(list(nova_lista))

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2) # round com o , 2 no final arredonda 2 casas decimais
    return p # esse p retorna a linha inteira do dicionário
novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)


# a função lambda abaixo não manipula o dicionário como desejamos fazer com a função acima
# precos = map(lambda p: p['preco'], produtos) # retornando o valor da chave preco
#
# for preco in precos:
#     print(preco)

#####################################################################

def aumenta_idade(p):
    p['idade'] = round(p['idade'] * 1.20) # round sem valor arredonda sem casas decimais
    return p


nomes = map(aumenta_idade, pessoas)

# nomes = map(lambda p: p['nome'], pessoas) # apenas selecionando as pessoas

for pessoa in nomes:
    print(pessoa)

# ourta forma de fazer adicionando um campo

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20) # round sem valor arredonda sem casas decimais
    return p


nomes = map(aumenta_idade, pessoas)

# nomes = map(lambda p: p['nome'], pessoas) # apenas selecionando as pessoas

for pessoa in nomes:
    print(pessoa)