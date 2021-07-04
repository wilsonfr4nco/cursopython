#  Indices = iterável
#        0123456789.......................33
frase = 'O rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
input_do_usuario = input('Qual letra deseja colocar maiúscula: ')

# Iteração: percorrer cada um de seus elementos
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
