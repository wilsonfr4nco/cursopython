"""
Módulos padrão do Python, são arquivos .py (que contém código python) e servem para expandir...
... as funcionalidasdes padrão da liguagem.
Documentacao dos modulos padrao do python https://docs.python.org/3/py-modindex.html
"""
# caso eu precise de um módulo e não tenha ele instalado, é só digitar no terminal: pip install nome-do-modulo
# módulo para randomização
from random import randint as randint2

def randint(*args):
    return 'hahaha'

# números para mega sena

for i in range(6):
    print(randint2(1,60))

# importar tudo de um módulo utilizando *
from random import *

print(randbytes(10))

# outra forma de importar é listando com vírgulas
from random import randint, randbytes
print(randint(32,33), randbytes(99))