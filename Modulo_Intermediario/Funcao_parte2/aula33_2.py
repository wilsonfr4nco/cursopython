# Função retornando tuplas


def dumb():
    return 'wilson', 'camila'

print(dumb())
var = dumb()

print(var, type(var))  # Tupla é uma lista que não pode ser alterada
# print()
print()

print(var[1], type(var))
