from time import sleep

print('\033[36m-=-'*9)
print('PEDRA, PAPEL E TESOURAAAAAA')
print('-=-'*9)
print('\033[m')

from random import choice
ppt = ['PEDRA', 'PAPEL', 'TESOURA', 'PEDRA', 'PAPEL', 'TESOURA']
result = choice(ppt)


eu = input('\033[32mDigite sua resposta -> ').upper()

print('Computador jogou -> {}\033[m'.format(result))
print('\033[35mANALIZANDO...\033[m')
sleep(2)
print('')

if eu == result and eu == 'PAPEL' and result == 'PAPEl':
    print('\033[33mEMPATE, PAPEL COM PAPEL NÃO DA NADA')

elif eu == 'PAPEL' and result == 'PEDRA':
    print('\033[34mPAPEL ENROLOU PEDRA')
    print('\033[35mVocê ganhou do computador!')

elif eu == 'PAPEL' and result == 'TESOURA':
    print('\033[34mTESOURA CORTOU O PAPEL')
    print('\033[31mO computador ganhou de você')


elif eu == result and eu == 'PEDRA' and result == 'PEDRA':
    print('\033[33mEMPATE, PEDRA COM PEDRA NÃO DA NADA')

elif eu == 'PEDRA' and result == 'PAPEL':
    print('\033[34mPAPEL ENROLOU A PEDRA')
    print('\033[31mO computador ganhou de você')

elif eu == 'PEDRA' and result == 'TESOURA':
    print('\033[34mPEDRA QUEBROU A TESOURA')
    print('\033[35mVocê ganhou do computador!')


elif eu == result and eu == 'TESOURA' and result == 'TESOURA':
    print('\033[33mEMPATE, TESOURA COM TESOURA NÃO DA NADA')

elif eu == 'TESOURA' and result == 'PEDRA':
    print('\033[34mPEDRA QUEBROU A TESOURA')
    print('\033[31mO computador ganhou de você')

elif eu == 'TESOURA' and result == 'PAPEL':
    print('\033[34mTESOURA CORTOU O PAPEL')
    print('\033[35mVocê ganhou do computador!')

if eu != 'TESOURA' and eu != 'PAPEL' and eu != 'PEDRA':
    print('\033[31mResposta invalida, tente novamente!')