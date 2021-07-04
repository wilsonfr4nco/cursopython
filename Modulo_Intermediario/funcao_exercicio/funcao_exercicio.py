"""
1 - Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada
"""

""""
def funcao1(valor):
    print(valor)
    return valor

def funcao2(recebe):
    return recebe

valor = funcao2(4)
funcao1(valor)
"""

"""
2 - Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o valor da funcao2 executada. Faça a funcao1
executar duas funções que recebam um número diferente de argumentos
"""

def funcao3(valor2, teste):
    print(valor2, teste)
    return valor2

def funcao4(valor3):
    valor3 += 1
    print(valor3)

def funcao5(valor4, valor5):
    valor4 += 1
    valor5 += 3
    print(valor4, valor5)

recebe, teste = funcao5(8, 9), funcao4(9)
funcao3(recebe, teste)


