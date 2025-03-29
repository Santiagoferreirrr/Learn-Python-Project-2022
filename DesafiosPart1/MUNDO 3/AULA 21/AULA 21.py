"""
def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Por Santiago Ferreira
    '''
    c = i
    while c <= f:
        print(f''
              f'{c}', end='')
        c += p
    print('FIM!')

help(contador)

def somar(a=0, b=0, c=0):
    '''
    -> Faz somar de três valores e mostrar o resultado na tela
    :param a: o primeiro valor
    :param b: o primeiro valor
    :param c: o priemiro valor
    Por Santiago Ferreira
    '''
    s = a + b + c
    print(f'A soma vale {s}')

somar(2, 5, 3)
somar(3, 2)

print()

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print()
print(f'A fora vale {a}')
print()

def somar(a=0, b=0, c=0):
    '''
    -> Faz somar de três valores e mostrar o resultado na tela
    :param a: o primeiro valor
    :param b: o primeiro valor
    :param c: o priemiro valor
    Por Santiago Ferreira
    '''
    s = a + b + c
    return s

r1 = somar(2, 5, 3)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
"""

def fatorial (num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

print()

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
