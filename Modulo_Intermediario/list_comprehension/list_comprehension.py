"""
List Comprehension
"""


l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1] # realizar interação de maneira simplificada.
print(ex1)
print()
#################################################################
ex2 = [v * 2 for v in l1] # Cada número da lista l1 multiplicado por 2
print(ex2)
print()
#################################################################
ex3 = [(v, v2) for v in l1 for v2 in range(3)] # realizando dois for em uma linha
print(ex3)
print()
#################################################################
l2 = ['wilson', 'camila', 'ringo', 'esher', 'jimi', 'kafka']
ex4 = [v.replace('i', '1') for v in l2] # substituindo letras das palavras em uma frase
print(ex4)
print()
#################################################################
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
)
ex5 = [(y, x) for x, y in tupla] # chaves invertidas na lista que virou depois dicionário
ex5 = dict(ex5)
print(ex5)
print(ex5['valor2'])
print()
##################################################################
l3 = list(range(100))
print(l3)
ex6 = [v for v in l3 if v % 2 ==0] # Seleciona todos os números divisíveis por 2
print(ex6)
ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0] # Seleciona todos os números divisíveis por 3 e por 8
print(ex7)
ex8 = [v if v % 3 == 0 else 'Não é' for v in l3] # números não divisíveis por 3 substituidos por "Não é"
print(ex8)
