"""
3 - Crie uma função que receba 2 números. Oprimeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return)
o valor do primeiro número somado do aumento do percentual do mesmo.
"""

def percentual(num, perc):
     num1 = num + (num * (perc / 100))
     return num + num1

print(percentual(100, 10))


