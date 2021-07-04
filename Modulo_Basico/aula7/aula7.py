nome = 'Wilson Franco'
idade = 43
altura = 1.78
e_maior = idade > 18
peso = 83
imc = peso / (altura * altura)


print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # o .2f é o ponto flutuante com 2 casas decimais
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))  # ordem das variáveis nas chaves
print('{2} tem {1} anos  e seu imc é {0}'.format(nome, idade, imc))  # ordem declarada das variáveis nas chaves
print('{n} tem {i} anos  e seu imc é {im}'.format(n=nome, i=idade, im=imc))  # variável da variável
