# a função filter trabalha com valores verdadeiros ou falsos ( o que for true é mantido na lista e o false é removido)

from listas import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
# nova_lista = [x for x in lista if x > 5] # similar ao exemplo acima.
print(list(nova_lista))

nova_lista2 = filter(lambda p: p['preco'] > 50, produtos)
for produto in nova_lista2:
    print(produto)

# abaixo temos um exemplo igual o de cima, mas sem o lambda
def filtra(produto):
    if produto['preco'] > 50:
        return True
nova_lista3 = filter(filtra, produtos)
