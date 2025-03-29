print('\033[33m===== CALCULADORA =====\033[m')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

v = ''

while v != 5:
    print('''
    [1] -> SOMAR
    [2] -> MULTIPLICAR
    [3] -> MAIOR
    [4] -> NOVOS NÚMEROS
    [5] -> SAIR DO PROGRAMA
    ''')
    v = int(input('Escolha umas das opções: '))

    if v == 1:
        print('Opção escolhida: \033[35mSOMA -> {} + {} = {}\033[m'.format(n1, n2, n1+n2))

    elif v == 2:
        print('Opção escolhida: \033[35mMULTIPLICAR -> {} * {} = {}\033[m '.format(n1, n2, n1*n2))

    elif v == 3:
        maior = n2
        if n1 > n2:
            maior = n1

        print('Opção escolhida: \033[35mMAIOR -> {}\033[m'.format(maior))

    elif v == 4:
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite um novo outro valor: '))

    elif v > 5: print('\033[31mOpção invalida! TENTE NOVAMENTE!!!\033[m')
print('\033[32mFIM DO PROGRAMA!')