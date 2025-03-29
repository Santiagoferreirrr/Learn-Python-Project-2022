ano = int(input('Em que ano você nasceu? '))
from datetime import date
year = date.today().year
print('')
id = year - ano
print('Você tem {} anos'.format(id))
print('')
if id <= 9:
    print('Classificação: MIRIM')

elif id <= 14:
    print('Classificação: INFANTIL')

elif id <= 19:
    print('Classificação: JUNIOR')

elif id <= 25:
    print('Classificação: SÊNIOR')

else: print('Classificação: MASTER')