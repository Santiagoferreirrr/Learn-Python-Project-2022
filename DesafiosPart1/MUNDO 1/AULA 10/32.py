ano = int(input('\033[36mQue ano quer analisar? Coloque 0 para analisar o ano atual: '))
from datetime import date

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 and ano % 400 == 0:
    print('\033[32mÉ Bissexto')

else:print('\033[31mNão é Bissexto')