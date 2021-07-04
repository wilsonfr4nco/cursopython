# fazendo cast com dicionário

lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

# como tenho um par eu posso converter para dicionário.
# posso também converter tuplas para dicionário, o que importa é ter chaves e valores.

d1 = dict(lista)

print(d1)

d1.pop('c3') #removeu um ítem
print(d1)

d2 = {
    1:2,
    2:3,
    4:5,
}

d1.update(d2) # contatenação
print(d1)