from time import sleep

'''def contador(ini, fim, pas):
    print('-='*25)
    print(f'{"Iniciando contagem de 1 até 10, de 1 em 1!":^50}')
    print()
    for c in range(1, 11):
        print(f'{c:^3}', end=" ")
        sleep(0.3)
    print(' ->   FIM!')

    print('-='*25)
    print(f'{"Iniciando contagem de 10 até 0, de 2 em 2!":^50}')
    print()
    for r in range(10, -1, -2):
        print(f'{r:^3}', end=' ')
        sleep(0.3)
    print(' ->   FIM!')

    print('-='*25)
    print(f'{"Agora é a sua vez de personalizar a contagem!":^50}')
    ini = int(input('Início: '))
    fim = int(input('Fim: '))
    pas = int(input('Passo: '))
    print('-='*25)
    print(f'{f"Contagem de {ini} até {fim} de {pas} e {pas}!":^50}')
    print()
    for l in range(ini, fim+1, pas):
        print(f'{l:^2}', end=' ')
        sleep(0.3)
    print('->  FIM!')

contador(1, 2, 3)'''

def contador(i, f, p):
    if p < 0:
        p *= -1

    if p == 0:
        p = 1

    print('-='*20)
    print(f'A contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='  ')
            sleep(0.3)
            cont += p
        print('->  FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='  ')
            sleep(0.3)
            cont -= p
        print('->  FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de personalizar sua contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)