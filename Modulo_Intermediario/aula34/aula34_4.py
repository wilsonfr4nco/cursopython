"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for divivível
por 5 retorne buzz. Se o parâmetro da função for divisível por 5 e 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

def fb(num):
    conta1 = num % 3
    conta2 = num % 5
    if not conta1 and not conta2:
        return 'FizzBuzz'
    elif not conta1:
        return 'Fizz'
    elif not conta2:
        return 'Buzz'
    return num

if __name__ == '__main__':


    print(fb(9))
    print(fb(5))
    print(fb(15))
    print(fb(4))
