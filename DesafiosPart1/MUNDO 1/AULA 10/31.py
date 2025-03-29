dist = int(input('\033[33mDigite a distância da viagem: '))

if dist > 200:
    print('\033[34mO preço da sua passagem será de R${:.2f}'.format(dist * 0.45))
else: print('\033[34mO preço da sua passagem será de R${:.2f}'.format(dist * 0.50))

#pre = dist * 0.50 if dist <= 200 else dist * 0.45 #OUTRA FORMA DE SE FAZER
#print('O preço da sua passagem será de R${:.2f}'.format(pre))

