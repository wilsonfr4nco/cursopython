'''
Geradores, iteradores e iteráveis

Um iterador vai te dar um valor de cada vez.
geradores vão ser utilizandos quando não se quer utilizar muita memória.

'''
import sys
import time
# o exemplo abaixo mostra o quando de memória é utilizada pois se armazena toda a informação na memória
# o gerador é para armazenar apenas o que for ser utilizado.
lista = list(range(19000))
print(sys.getsizeof(lista))

# Função com gerador

def gera():
    for n in range(100):
        yield n # o "yield" é quem faz acontecer o gerador.
 #       time.sleep(0.1)

g = gera()

for v in g:
    print(v)

# a maneira mais simples de criar gerador é com listcomprehension usando parênteses

l1 = [x for x in range(1999000)]
l2 = (x for x in range(1999000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))