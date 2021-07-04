"""
Operadores lógicos - AND, OR, NOT, IN e NOT IN
"""

# Operador AND só é verdade quando as duas condições forem verdadeiras
# Operador OR só é falso quando as duas condições forem falsas
# Operador NOT inverte o valor.
# Se a string igual a vazio é considerado como falso '' e o inteiro igual a 0 é considerando tembém falso.
# operador IN é o mesmo que dizer 'está contido'
# operador NOT IN não está contido.

nome = input('Digite uma plavra: ')
letra = input('Digite uma letra: ')

if letra in nome:
    print(f'A Letra {letra} está contida no nome {nome}')
else:
    print(f'A letra {letra} não está contida no nome {nome} ')
