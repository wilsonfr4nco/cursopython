"""
Um site com compras de produtros e deve-se fazer um código para somar os valores dos itens escolhidos
Somar os valores do carrinho
"""


carrinho = []

carrinho.append(('produto 1', 20))
carrinho.append(('produto 2', 50))
carrinho.append(('produto 2', 50))
carrinho.append(('produto 3', 30))
carrinho.append(('produto 3', 30))

total = sum([float(y) for x, y in carrinho])
print(total)