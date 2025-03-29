'''Escreva um programa que faça o computador "pensar" em um número...'''

from time import sleep
print('\033[36m-=-' * 26)
print('\033[0;34mO computador está pensando em um número de 0 a 5, adivinhe e ganhe 2 dolares!')
print('\033[36m-=-' * 26)

sleep(2)

#from random import choice
#lista = ['0', '1', '2', '3',' 4', '5']
#pc = choice(lista)


from random import randint
pc = randint(0, 5)
num = int(input('\033[34mDigite seu palpite agora: '))
print('\033[35mANALIZANDO...')
sleep(3)


#if num == esc:
if num == pc:
    print('\033[32m=x' * 21)
    print('Parabéns, você acertou e ganhou 2 dolares')
    print('=x' * 21)
else:
    print('\033[31m=x' * 14)
    print('''   Que pena, você errou...
o número escolhido foi {}! ;('''.format(pc))
    print('=x' * 14)


