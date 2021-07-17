"""
str - string
"""

print('alguma coisa')
print("Aspas duplas")  # tudo dentro de aspas é string
print(123456)  # numero inteiro

# erro = print('essa é uma 'string' (str).')
print("essa é uma 'string' (str).")  # correto
r""""
 abaixo esse caractere de escape "\" faz poder ignorar o proximo caractere
 mas não fica bem escrito, é preferível utilizar o de cima alternando aspas simples
 com aspas compostas """
print('essa é uma \'string\' (str).')
print('essa é uma \n (str).')  # o caractere de escape seguido de n é uma quebra de linha.
print(r'essa é uma \n (str).')  # a letra r no inicio esta dizendo que tudo dentro das aspas nao é para executar
