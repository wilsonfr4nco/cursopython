"""
Funções DEF em python - *args **kwargs -
Parte 3
"""


# *args é uma convenção da comunidade python, pois basta usar o "*" para funcionar, ele é usado
# para valores que não são  strings
# **kwargs é uma convenção da comunidade python, pois basta usar "**" para funcionar, ele é usado
# para valores em strings
def func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome']) # dessa forma se as variáveis não tiverem valor dará erro
    idade = kwargs.get('idade') # dessa maneira se a variável idade não tiver valor o programa não retorna erro
    print(idade)


lista = [1,2,3,4,5]
lista2 = [43, 43, 23, 12, 12]
func(lista, 5)  # A lista fica como um ítem da tupla
func(*lista)  # Desempacotando a lista
func(1,2,3,4,5)
func(*lista, *lista2, nome='wilson', sobrenome='franco')

