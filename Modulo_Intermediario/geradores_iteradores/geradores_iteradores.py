'''
Geradores, iteradores e iteráveis

Um iterador vai te dar um valor de cada vez.
geradores vão ser utilizandos quando não se quer utilizar muita memória.

'''
lista = [1,2,3,4,5]

print(hasattr(lista, '__iter__')) # função builtin do hasarttr para saber se é um objeto iterável
# o for transforma a lista em um iterador

for v in lista:
    print(v) # lista transformada em iterador, mas ela por si mesma não é iterador e sim iterável

# o método __next__ da função hasattr revela se o objeto é ou não um iterador

print(hasattr(lista, '__next__'))

# transformando lista em um iterador
lista = iter(lista)
print(hasattr(lista, '__next__'))
# ao ser transformada em iterador a função next pode ser utilizada para iterar
print(next(lista))
print(next(lista))
print(next(lista))

