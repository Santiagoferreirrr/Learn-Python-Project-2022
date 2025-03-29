from time import sleep
from datetime import date
print('\033[35m:::' * 5)
print('SERVIÇO MILITAR')
print(':::' * 5)
print('')
ano = int(input('\033[32mAno que você nasceu -> '))
print('ANALIZANDO...')
sleep(2)
print('')
year = date.today().year
id = year - ano
print('\033[33mVocê tem {} anos'.format(id))
print('')
if id == 18:
    print('\033[mHora de se alistar!')

elif id < 18:
    print('Você ainda se alistará!')
    print('Falta {} ano(s)'.format(18-id))

elif id > 18:
    print('Já passou do tempo do seu alistamento!')
    print('Já faz {} anos que você deveria ter se alistado'.format(id-18))


