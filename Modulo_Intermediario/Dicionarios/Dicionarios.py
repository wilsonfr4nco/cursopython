"""
Dicionário, suporta uma chave(indíce) e um valor
"""

d1 = {'chave1':'valor da chave'}
d1['nova_chave'] = 'valor da nova chave'
print(d1)
print(d1['chave1'])
print()
print()
d2 = dict(chave1='valor da chave', chave2='valor da outra chave')
print(d2)

d3 = {'chave' : 'valor', 'chave' : 'valor', 'chave' : 'valor da chave real'} # a chave se repete e com isso
# só aparece o último valor da chave
d4 = {1: 'valor', 2: 'valor', 3: 'valor da chave real'}
print(d3)
print(d4)


print()
print()

# pode utilizar como chave qualquer valor imutável
d5 = {
    'str': 'valor',
    123: 'outro valor',
    (1,2,3,4): 'tupla',
}
print(d5[(1,2,3,4)])

if 'naoexiste' in d5:
    print(d1['naoexiste'])

print('Oi')
print()
print()
d5['naoexiste'] = 'agora existe' # criando chave e valor no dicionário
if 'naoexiste' in d5:
    print(d5['naoexiste'])

print('Oi')

##############################################

print(d5.get('nomedachave')) # como a chave não existe no dicionário o retorno é valor none
print(d5.update({'nova_chave': 'novo_valor'}))

del d5['str'] # apaga a chave e o valor do dicionário
print('str' in d5) # verificar se esta chave existe
print('str' in d5.keys()) # mesmo exemplo do de cima
print('valor' in d1.values()) # acessar os valores do dicionário