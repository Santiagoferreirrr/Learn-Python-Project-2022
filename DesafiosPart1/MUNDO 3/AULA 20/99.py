def maior(*par):
    print('-=' * 25)
    print('Analisando os valores passados...')
    print(f'{par} -> Foram informados {len(par)} valores ao todo.')
    print(f'O maior valor informado foi -> {max(par)}.')

'''from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')'''


maior(3, 4, 5, 7, 8)
maior(2, 4, 6)
maior(7, 1, 5, 9)