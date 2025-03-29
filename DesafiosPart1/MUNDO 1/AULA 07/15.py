dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
paga = (dias*60) + (km*0.15)
print('O valor a ser pago é de R${:.2F}'.format(paga))