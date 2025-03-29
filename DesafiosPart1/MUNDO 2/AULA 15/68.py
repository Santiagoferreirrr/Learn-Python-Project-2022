from random import randint

print('\033[35m=-='*10)
print('   VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*10)

vit = 0

while True:
    jogador = int(input('\033[mDigite um valor: '))
    pc = randint(0, 10)
    total = pc + jogador
    parouimpa = 'a'
    while parouimpa not in 'PI':
        parouimpa = str(input('Par ou Ímpar: ')).upper().strip()[0]
    print('')
    print(f'Você jogou {jogador} e o computador {pc}. Total deu {total}', end=' -> ')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    print('')

    if parouimpa == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vit += 1
            print('Vamos jogar novamente...')
        else:
            print('Você PERDEU!', end=' ')
            break
    elif parouimpa == 'I':
        if parouimpa % 2 == 1:
            print('Você VENCEU!')
            print('Vamos jogar novamente...')

        else:
            print('Você PERDEU!', end=' ')
            break

print(f'GAME OVER! Você venceu {vit} vezes.')
'''
    if parouimpa == result:
        print('\033[32m---'*22)
        print('Você GANHOU!', end=' ')
        print(f'Você jogou {jogador} e o computador {pc}. Total deu {total} e é {result}')
        print('Vamos jogar novamente...')
        print('---' * 22)
        vit += 1
        print('\033[m')

    else:
        print('\033[31m---'*22)
        print('GAME OVER!', end=' ')
        print(f'Você jogou {jogador} e o computador {pc}. Total deu {total} e é {result}')
        print('---' * 22)
        print('\033[m')
        print(f'\033[33mVocê teve {vit} vitórias consecutivas!')
        break
'''