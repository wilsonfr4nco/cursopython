"""
Documentação e funções built-in úteis
"""

num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

# verificar se a string pode ser convertida em número (consultar documentação do python)
# isnumeric isdigit isdecimal - essa funções são apenas para números positivos e inteiros

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(num2 + num1)
else:
    print('Caractere inválido para fazer soma!!')


