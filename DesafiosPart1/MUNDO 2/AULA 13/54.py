dmaior = 0
dmenor = 0

for x in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu -> '.format(x)))
    from datetime import date
    id = date.today().year - ano

    if id < 18:
        dmenor += 1
    elif id > 18:
        dmaior += 1

print('Ao total, são {} de menor e {} de maior!'.format(dmenor, dmaior))