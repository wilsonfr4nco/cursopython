"""
Tipos de dados

str - string (textos)
int - inteiro (número negativo ou positivo que não tenha ponto)
float - numero real ou ponto flutuante (número positivo ou negativo que tenha ponto) não se usa vírgula.
bool - booleando ou lógico (verdadeiro ou falso) tudo que é valor zerado ou vazio é avaliado como falso

"""

print('wilson', type('wilson'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))
print('l' == 'L', type('l' == 'l'))
print(bool())

print('wilson', type('wilson'), bool('wilson'))
print('10', type('10'), type(int('10')))
print(10 + 10)
