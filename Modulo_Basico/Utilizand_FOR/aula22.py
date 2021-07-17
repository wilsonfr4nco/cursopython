"""
For in  em python
função range(start=0, stop, step=1)
"""
texto = 'Python'
nova_string = ''

for letra in texto:
    print(letra)
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
