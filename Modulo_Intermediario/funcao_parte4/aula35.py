"""
Escopo de variável em python
"""

variavel = 'valor' # escopo global, acessível a todos os locais.

def func():
    print(variavel)

def func2():
    print(variavel)

func()
func2()