maior = 0
menor = 0
for x in range(1, 6):
    p = float(input('Peso da {}ª pessoa -> '.format(x)))
    if x == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('Maior peso lido foi de {}Kg!'.format(maior))
print('Menor peso lido foi de {}Kg!'.format(menor))