"""
Escopo de variável em python
"""

def func():
    variavel1 = 'wilson'
    return variavel1

def func2(arg):
    print(arg)

var = func()
func2(var)  # passando o valor de uma função para outra sem usar variável global
