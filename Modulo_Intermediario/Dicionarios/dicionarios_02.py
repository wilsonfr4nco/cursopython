d1 = {
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3' : 'tupla',
}

print(len(d1)) # vai falar quantos pares possuem no dicionário.

for k in d1:
    print(k) # print as chaves

for v in d1.values():
    print(v) # print só nos valores

for k in d1.items():
    print(k) # printa a chave e valor.
    print(k[0], k[1]) # print chave e valor separadamente

for k, v in d1.items():
    print(k,v) # print a chave o valor já separados. (desempacotado)

d2 = {
    'cliente1' : {
        'nome' : 'wilson',
        'sobrenome' : 'franco',

    },

    'cliente2': {
            'nome': 'camila',
            'sobrenome': 'cestari',

        },
}

for clientes_k, clientes_v in d2.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t {dados_k} = {dados_v}')