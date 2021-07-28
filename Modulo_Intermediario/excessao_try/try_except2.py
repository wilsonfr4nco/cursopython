"""
Tratando erros no python
"""

try:
    print(a)
except NameError as erro:
    print("Ocorreu um erro: ", erro)
except Exception as erro: # Exception é um coringa que qualquer erro se enquadra.
    print('Ocorreu um erro inesperado: ', erro)

try:
    a = []
    print(a[1]) # como indice 1 não existe na lista e não é Name error ele será exibido como erro de índice
except NameError as erro:
    print("Ocorreu um erro: ", erro)
except IndexError as erro:
    print('Erro de índice: ', erro)
except Exception as erro: # Exception é um coringa que qualquer erro se enquadra.
    print('Ocorreu um erro inesperado: ', erro)
else: # o else será executado se o try não tiver erro
    print("Código sem erro")
finally: # independente de ter ou não erro, sempre será executado.
    print("sempre executada")
# como o erro acima foi tratado o código continua sendo executado.

print("Continuação do código...")