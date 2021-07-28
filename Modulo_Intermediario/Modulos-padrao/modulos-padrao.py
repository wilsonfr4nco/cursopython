"""
Módulos padrão do Python, são arquivos .py (que contém código python) e servem para expandir...
... as funcionalidasdes padrão da liguagem.
Documentacao dos modulos padrao do python https://docs.python.org/3/py-modindex.html
"""
import sys # mostra dados do sistema operacional
print(sys.platform) # mostra qual é o sistema operacional

# para digitar menos código posso importa o mesmo módulo de outra maneira, conforme abaixo
from sys import platform
print(platform)

# também posso renomear o módulo da seguinte maneira
from sys import platform as so
print(so)
