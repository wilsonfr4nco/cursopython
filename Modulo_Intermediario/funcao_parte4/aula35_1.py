"""
Escopo de variável em python
"""

variavel = 'valor'  # escopo global

def func():
    print(variavel)

def func2():
    variavel = 'Outro valor'  # variável disponível apenas nessa função, não tem relação com qualquer outra variável
    print(variavel)

def func3():
    global variavel
    variavel = 'novo valor'  # agora essa é a mesma variável utilizada no inicio do programa
    print(variavel)


func()
func2()
func3()