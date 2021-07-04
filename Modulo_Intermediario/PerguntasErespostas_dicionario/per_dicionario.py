"""
Perguntas e respostas com dicionários
"""
# Código arrumado:
# perguntas = {
#     'pergunta 1' : {
#         'pergunta' : 'quanto é 2+2?',
#         'respostas' : {
#             'a' : '1',
#             'b' : '4',
#             'c' : '5',
#         }
#         'resposta_certa' : 'b',
#     }
# }

perguntas = {
    'pergunta 1' : {
        'pergunta' : 'quanto é 2+2?',
        'respostas' : {'a' : '1','b' : '4','c' : '5',},
        'resposta_certa' : 'b',
    },
    'pergunta 2' : {
        'pergunta' : 'quanto é 3x2?',
        'respostas' : {'a' : '4','b' : '10','c' : '6',},
        'resposta_certa' : 'c',
    },
    'pergunta 3' : {
        'pergunta' : 'quanto é 4x2?',
        'respostas' : {'a' : '4','b' : '8','c' : '6',},
        'resposta_certa' : 'b',
    },
    'pergunta 4': {
        'pergunta': 'quanto é 3x7?',
        'respostas': {'a': '21', 'b': '10', 'c': '6', },
        'resposta_certa': 'a',
    },
    'pergunta 5': {
        'pergunta': 'quanto é 3x5?',
        'respostas': {'a': '4', 'b': '10', 'c': '15', },
        'resposta_certa': 'c',
    },
}
print('Texto explicativo')
print()
resposta_certa = 0
for chave_pergunta, chave_resposta in perguntas.items():
    print(f'{chave_pergunta}: {chave_resposta["pergunta"]}')

    print('Escolhas as opções abaixo')
    for resposta_chaves, respostas_valores in chave_resposta['respostas'].items():
        print(f'[{resposta_chaves}]: {respostas_valores}')
    resposta_usuario = input('Sua resposta:')
    print()
    if resposta_usuario == chave_resposta['resposta_certa']:
        print('Você acertou!!!')
        resposta_certa += 1
    else:
        print('Você errou!!')


qtd_perguntas = len(perguntas)
porcentagem_acerto = resposta_certa / qtd_perguntas * 100
print(f'Você acertou {porcentagem_acerto}% de respostas')