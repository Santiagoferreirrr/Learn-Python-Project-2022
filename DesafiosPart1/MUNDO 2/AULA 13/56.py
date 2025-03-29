somaid = 0
mediaid = 0
maioridh = 0
nomev = ''
totm20 = 0
for x in range(1, 5):
    print('-=-=- {}ª PESSOA -=-=-'.format(x))
    n = str(input('Nome: ')).strip()
    id = int(input('Idade: '))
    sx = str(input('Sexo [M/F]: ')).strip()
    somaid += id
    if x == 1 and sx in 'Mm':
        maioridh = id
        nomev = n
    if sx in 'Mm' and id > maioridh:
        maioridh = id
        nomev = n
    if sx in 'Ff' and id < 20:
        totm20 += 1
mediaid = somaid / 4
print('A média de idade do grupo é de {} anos'.format(mediaid))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridh, nomev))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm20))