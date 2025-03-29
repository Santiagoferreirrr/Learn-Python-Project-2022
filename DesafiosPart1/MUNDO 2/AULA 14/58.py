'''Escreva um programa que faça o computador "pensar" em um número...'''

from time import sleep
print('\033[36m-=-' * 26)
print('\033[0;34mO computador está pensando em um número de 0 a 10, adivinhe e ganhe 2 dolares!')
print('\033[36m-=-' * 26)

sleep(2)

from random import randint
pc = randint(0, 10)
num = 1
cont = 1
while num != pc:
    num = int(input('\033[34mDigite seu palpite agora: '))
    print('\033[35mANALIZANDO...')
    sleep(1)
    if num == pc:
        print('\033[32m=x' * 49)
        print('Parabéns, você acertou, a resposta era {} e você deu {} palpites até acertar, você ganhou 2 dolares'.format(pc, cont))
        print('=x' * 49)
    else:
        print('\033[31m=x' * 14)
        print('''   Que pena, você errou...
      TENTE NOVAMENTE!''')
        print('=x' * 14)
        cont += 1
        if num < pc:
            print('\033[35m   Mais... tente novamente')
        else:
            print('\033[35m  Menos... tente novamente')