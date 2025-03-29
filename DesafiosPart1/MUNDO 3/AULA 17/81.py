num = []
s = ' '
while True:
    num.append(int(input('Digite um número: ')))
    num.sort(reverse=True)

    if 5 in num:
        s = 'O valor 5 foi digitado e está na lista'
    else: s = 'Não foi encontrado o valor 5 na lista'

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('-=-'*25)
print(f'Foram digitados {len(num)} números!')
print(f'A lista dos valores em forma decrescente é {num}')
print(f'{s}')