from time import sleep
c = ('\033[m',   #0 - SEM COR
    '\033[41m',  #1 - VERMELHO
    '\033[42m',  #2 - VERDE
    '\033[43m',  #3 - AMARELO
    '\033[44m',  #4 - AZUL CLARO
    '\033[45m',  #5 - ROXO
    '\033[46m',  #6 - CIANO
    '\033[7;30m' #7 - BRANCO
    )
def inthelp(func):
    tit(f'ACESSANDO O MANUAL DO COMANDO \'{func}\'', 4)
    print(c[7], end ='')
    help(func)
    print(c[0], end='')
    sleep(2)
def tit(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)
func = ''
while True:
    tit('SISTEMA DE AJUDA PyHELP', 2)
    func = str(input('Função ou Biblioteca -> '))
    if func.upper() == 'FIM':
        print('~'*20)
        print(tit)
        print('~'*20)
        break
    else:
        inthelp(func)
tit('ATÉ LOGO!', 1)
