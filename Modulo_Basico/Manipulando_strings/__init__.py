cpf = '94039879520'
dig1 = '3'
dig2 = '5'
cpf2 = cpf[:9] + dig1 + dig2

if cpf == cpf2:
    print('cpf válido')
else:
    print('cpf inválido')

