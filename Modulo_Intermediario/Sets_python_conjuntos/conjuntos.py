"""
Conjuntos - similares a lista e tuplas com a diferença que os "sets" suportam apenas elementos únicos,
não tem índice também
sets: não têm par de chave e valor.
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference  (Elementos que estao nos dois sets, mas nao em ambos)

Muito utilizado para elimintar elementos duplicados em uma lista
"""

s1 = {1,2,3,4,5,6}
print(s1)

for v in s1:
    print(v)

s1 = set() # criando um set vazio
s1.add(1)
s1.add(2)
print(s1)
s1.discard(2)
print(s1)

s1 = set()
s1.add('python')
print(s1)
s1.update('python') # dessa forma será iterável sem respeitar a ordem

print(s1)
print()
s1 = set()
s1.update([1,2,3,4,5], {5,6,7,8})
print(s1)

print('removendo elementos duplicados')
l1 = [1,2,1,1,2,3,4,5,6,6,6,6,6,7,8,9,'wilson', 'wilson']
l1 = set(l1)
print(l1)

l1 = list(l1)

print(l1)

# outras funções da lista.

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2 # função union com "|"
print(s3)
s4 = s1 & s2 # só mostra os elemento iguais.
print(s4)
s5 = s1 - s2 # só mostra o elemento diferente do item da esquerda "s1"
print(s5)
s6 = s1 ^ s2 # mostra o que tem de diferente nos dois sets.
print(s6)

l1 = ['wilson', 'camila', 'ringo']
l2 = ['jimmi', 'escher', 'kafka', 'jimmi']

l1 = list(set(l1))
l2 = list(set(l2))








