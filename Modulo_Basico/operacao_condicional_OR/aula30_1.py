"""
Operação condicional com operador OR
"""
# Lembrando que vazio é falso e com conteúdo é verdadeiro
nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada!')

# simplificando o exemplo acima

nome = input('Qual o seu nome? ')
print(nome or None or False or 0 or 'Você não digitou nada!') # sequência de or
