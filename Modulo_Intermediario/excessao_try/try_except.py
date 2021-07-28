"""
Tratando erros no python
"""
# Tudo que estiver dentro do try será verificado se possui erro.
try:
    print(a)

# Quando após o except não é especificado nada, qualquer erro será tratado conforme o código no except
except:
    print('Erro!')

# o código abaixo retornará um erro do tipo "NameError" , podemos então tratar esse erro no except
# print(a)

try:
    print(a)
except NameError as erro: # coloquei o erro na variável "erro"
    print("Ocorreu um erro: ", erro)

# como o erro acima foi tratado o código continua sendo executado.

print("Continuação do código...")