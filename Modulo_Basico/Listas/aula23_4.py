"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

secreto = input('Digite a palavra secreta: ')
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print("Isso não vale, digite apenas uma letra!")
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Parabéns você ganhou!\nA palavra secreta é: {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está incompleta: {secreto_temporario}')
    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.')
# print(secreto_temporario)
