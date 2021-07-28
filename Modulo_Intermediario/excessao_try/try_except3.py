"""
Tratando erros no python
"""

try:
    print("casa")
    try: # esse try só é executado se a linha anterior não contiver erro.
        print('continuando a tratar erro', a)
    except Exception as falha:
        print('Novo erro tratado: ', falha)
except NameError as erro:
    print("Ocorreu um erro: ", erro)
except Exception as erro: # Exception é um coringa que qualquer erro se enquadra.
    print('Ocorreu um erro inesperado: ', erro)



# como o erro acima foi tratado o código continua sendo executado.

print("Continuação do código...")