print('---'*10)
print('   LOJA SUPER PAGUE MENOS')
print('---'*10)

gast = prodmais1000 = menor = cont = 0
barato = ' '

while True:
    prod = str(input('Nome do Produto: '))
    pre = float(input('Preço: R$'))
    cont += 1
    gast += pre
    if pre > 1000:
        prodmais1000 += 1
    if cont == 1 or pre < menor:
        menor = pre
        barato = prod

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if resp == 'N':
        break

print('')
print('==='*4, end='')
print(' FIM DO PROGRAMA ',end='')
print('==='*4)
print(f'O total gasto foi de R${gast:.2f}')
print(f'{prodmais1000} produtos custaram mais de R$1000.00!')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')